# -*- mode: python; coding: utf-8 -*-

assert str is not bytes

import random
import json
import base64
from urllib import parse as url_parse
from urllib import request as url_request

import bottle
from . import layout

#PAYPAL_SERVER_URL = 'https://api.sandbox.paypal.com'
#PAYPAL_APP_SECRET = \
#        'AZ9VyxA8DMd9FcuyhUq9WY0TZS1PXcyo7SKE15Mq1KJifB0mhOlt6a-GxW8z' \
#        ':' \
#        'EL2PvRDTKVpUL4CiV7dSXltY_wnPrYOYN7XsycNsAT-AlJMMD8O540X4kNl3'

PAYPAL_SERVER_URL = 'https://api.paypal.com'
PAYPAL_APP_SECRET = \
        'AVLaKxDE91TyFzQsjDWK8AOeTEOb_5LuM5YkNn58Gf3XiM9oogFs3-XUnion' \
        ':' \
        'EGF5MRCoWsqJPNRAvzesqU0KwsEPC_lWKo_V3Gc-Nxffw0DWfWAT3jBL5107'

DEFAULT_TIMEOUT = 60.0
DEFAULT_READ_LIMIT = 10000000

def home_view():
    def create_lot(title, amount):
        lot_id = random.randrange(1000000000, 2000000000)
        
        return (
                lot_id,
                title,
                amount,
                '{}/paypal-experiment/buy?{}'.format(
                        bottle.request.environ['app.ROOT'],
                        url_parse.urlencode({'lot_id': lot_id}),
                        ),
                )
    
    lot_list = (
            create_lot('Баночка огурцов [бутылка #{}]'.format(random.randrange(1000000, 2000000)), '1.50'),
            create_lot('Коробок говнеца [упаковка #{}]'.format(random.randrange(10000000, 20000000)), '2.00'),
            )
    
    # BEGIN HACK:
    #   на самом деле нужно использовать БАЗУ ДАННЫХ, а не Cookie (Cookie)
    #   здесь использованы Cookie -- только для проверки концепции,
    #
    #   здесь мы создаём новые лоты. в случае реального магазины --
    #       лоты это были бы товары, и они УЖЕ были БЫ созданы.
    #
    #   в случае виртуальных услуг -- лоты нужно всё же создавать здесь (а просроченные лоты удалять).
    #       но всё равно нужно это делать в БАЗЕ ДАННЫХ, а не в Cookie.
    
    for lot in lot_list:
        lot_id = lot[0]
        bottle.response.set_cookie('paypal_experiment__db_emu__{}'.format(lot_id), {
                'status': 'opened',
                'title': lot[1],
                'amount': lot[2],
                }, secret='ib9o9D74', max_age=7200, path='/')
    
    # END OF HACK
    
    return layout.render_layout(
            title='Paypal Experiment',
            menu_name='paypal_experiment/home',
            content_file='paypal_experiment/home.mako',
            content__lot_list=lot_list,
            )

def get_access_token(opener):
    res = opener.open(url_request.Request(
            url_parse.urljoin(PAYPAL_SERVER_URL, 'v1/oauth2/token'),
            data=url_parse.urlencode({
                    'grant_type': 'client_credentials',
                    }).encode(errors='replace'),
            headers={
                    'Authorization': 'Basic {}'.format(
                            base64.b64encode(PAYPAL_APP_SECRET.encode(errors='replace')).decode(errors='replace'),
                            ),
                    },
            ), timeout=DEFAULT_TIMEOUT)
    
    res_data = json.loads(res.read(DEFAULT_READ_LIMIT).decode(errors='replace'))
    access_token = res_data.get('access_token')
    
    if not isinstance(access_token, str) or not access_token:
        bottle.abort(500, 'no access_token')
    
    return access_token

def buy_view():
    lot_id = bottle.request.params.getunicode('lot_id')
    
    if not lot_id:
        bottle.abort(500, 'missing some params')
    
    # BEGIN HACK:
    #   на самом деле нужно использовать БАЗУ ДАННЫХ, а не Cookie (Cookie)
    #   здесь использованы Cookie -- только для проверки концепции,
    #
    #   здесь мы резервируем лоты. переводим их в состояние "занято".
    #
    #   важно чтобы мы делали бы выборку --
    #           только среди тех лотов чьё состояние "открыто"
    
    db_entry = bottle.request.get_cookie('paypal_experiment__db_emu__{}'.format(lot_id),
            secret='ib9o9D74')
    
    if not db_entry or db_entry.get('status') != 'opened':
        bottle.abort(500, 'lot not found')
    
    title = db_entry.get('title')
    amount = db_entry.get('amount')
    
    db_entry['status'] = 'buy_busy'
    bottle.response.delete_cookie('paypal_experiment__db_emu__{}'.format(lot_id),
            secret='ib9o9D74', path='/')
    bottle.response.set_cookie('paypal_experiment__db_emu__{}'.format(lot_id),
            db_entry, secret='ib9o9D74', max_age=7200, path='/')
    
    # END OF HACK
    
    opener = url_request.build_opener()
    access_token = get_access_token(opener)
    
    full_root_url = '{}://{}{}'.format(
            bottle.request.environ['wsgi.url_scheme'],
            bottle.request.environ['HTTP_HOST'],
            bottle.request.environ['app.ROOT'],
            )
    
    data = {
            'intent': 'sale',
            'redirect_urls': {
                    'return_url': '{}/paypal-experiment/buy-return?{}'.format(
                            full_root_url,
                            url_parse.urlencode({'lot_id': lot_id}),
                            ),
                    'cancel_url': '{}/paypal-experiment/buy-cancel'.format(full_root_url),
                    },
            'payer': {
                    'payment_method': 'paypal',
                    },
            'transactions': [
                    {
                            'amount': {'total': amount, 'currency': 'RUB'},
                            'description': title,
                            },
                    ],
            }
    
    res = opener.open(url_request.Request(
            url_parse.urljoin(PAYPAL_SERVER_URL, 'v1/payments/payment'),
            data=json.dumps(data).encode(errors='replace'),
            headers={
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer {}'.format(access_token),
                    },
            ), timeout=DEFAULT_TIMEOUT)
    
    res_data = json.loads(res.read(DEFAULT_READ_LIMIT).decode(errors='replace'))
    res_links = res_data.get('links')
    
    if not isinstance(res_links, (tuple, list)) or not res_links:
        bottle.abort(500, 'no res_links')
    
    for res_link in res_links:
        if not isinstance(res_link, dict):
            continue
        
        res_link_rel = res_link.get('rel')
        res_link_href = res_link.get('href')
        
        if not isinstance(res_link_rel, str) or res_link_rel != 'execute' or \
                not isinstance(res_link_href, str) or not res_link_href:
            continue
        
        break
    else:
        bottle.abort(500, 'no res_link_href')
    
    # BEGIN HACK:
    #   на самом деле нужно использовать БАЗУ ДАННЫХ, а не Cookie (Cookie)
    #   здесь использованы Cookie -- только для проверки концепции,
    #
    #   запиминаем данные для перевода денег
    
    db_entry['paypal_execute'] = res_link_href
    bottle.response.delete_cookie('paypal_experiment__db_emu__{}'.format(lot_id),
            secret='ib9o9D74', path='/')
    bottle.response.set_cookie('paypal_experiment__db_emu__{}'.format(lot_id),
            db_entry, secret='ib9o9D74', max_age=7200, path='/')
    
    # END OF HACK
    
    for res_link in res_links:
        if not isinstance(res_link, dict):
            continue
        
        res_link_rel = res_link.get('rel')
        res_link_href = res_link.get('href')
        
        if not isinstance(res_link_rel, str) or res_link_rel != 'approval_url' or \
                not isinstance(res_link_href, str) or not res_link_href:
            continue
        
        break
    else:
        bottle.abort(500, 'no res_link_href')
    
    bottle.redirect(res_link_href)

def buy_return_view():
    lot_id = bottle.request.params.getunicode('lot_id')
    payer_id = bottle.request.params.getunicode('PayerID')
    
    if not lot_id or not payer_id:
        bottle.abort(500, 'missing some params')
    
    # BEGIN HACK:
    #   на самом деле нужно использовать БАЗУ ДАННЫХ, а не Cookie (Cookie)
    #   здесь использованы Cookie -- только для проверки концепции,
    #
    # проверяем что с лотом всё нормально. и извлекаем данные для перевода деньг
    
    db_entry = bottle.request.get_cookie('paypal_experiment__db_emu__{}'.format(lot_id),
            secret='ib9o9D74')
    
    if not db_entry or db_entry.get('status') != 'buy_busy':
        bottle.abort(500, 'lot not found')
    
    title = db_entry.get('title')
    amount = db_entry.get('amount')
    paypal_execute_url = db_entry.get('paypal_execute')
    
    # END OF HACK
    
    opener = url_request.build_opener()
    access_token = get_access_token(opener)
    
    data = {
            'payer_id': payer_id,
            }
    
    res = opener.open(url_request.Request(
            paypal_execute_url,
            data=json.dumps(data).encode(errors='replace'),
            headers={
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer {}'.format(access_token),
                    },
            ), timeout=DEFAULT_TIMEOUT)
    
    res_data = json.loads(res.read(DEFAULT_READ_LIMIT).decode(errors='replace'))
    
    # BEGIN HACK:
    #   на самом деле нужно использовать БАЗУ ДАННЫХ, а не Cookie (Cookie)
    #   здесь использованы Cookie -- только для проверки концепции,
    #
    # закрываем лот.
    
    db_entry['status'] = 'closed'
    bottle.response.delete_cookie('paypal_experiment__db_emu__{}'.format(lot_id),
            secret='ib9o9D74', path='/')
    bottle.response.set_cookie('paypal_experiment__db_emu__{}'.format(lot_id),
            db_entry, secret='ib9o9D74', max_age=7200, path='/')
    
    # END OF HACK
    
    from pprint import pformat
    
    return layout.render_layout(
            title='Result of Paypal Experiment',
            menu_name='paypal_experiment/home',
            content_file='paypal_experiment/buy_return.mako',
            content__lot_title=title,
            content__lot_amount=amount,
            content__paypal_res_data=pformat(res_data),
            )

def buy_cancel_view():
    bottle.redirect('{}/paypal-experiment'.format(bottle.request.environ['app.ROOT']))

def add_routes(app, root):
    app.route('{}/paypal-experiment'.format(root), callback=home_view)
    app.route('{}/paypal-experiment/buy'.format(root), callback=buy_view)
    app.route('{}/paypal-experiment/buy-return'.format(root), callback=buy_return_view)
    app.route('{}/paypal-experiment/buy-cancel'.format(root), callback=buy_cancel_view)
