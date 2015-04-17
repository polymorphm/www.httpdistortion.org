# -*- mode: python; coding: utf-8 -*-

assert str is not bytes

import os, os.path
import bottle
from mako import lookup as mako_lookup
from . import simple_page_views
from . import paypal_experiment_views

STATIC_DIR = os.path.join(os.path.dirname(__file__), 'static')
TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), 'templates')
DEFAULT_TITLE = 'Согласования и Разрешения в Пензе'
DEFAULT_DESCRIPTION = 'Согласования и Разрешения в Пензе. Получить разрешение на строительство в Пензе. Узаконить перепланировку в Пензе. Согласовать проект в Пензе. Дома Пензы. Межевание земельного участка в Пензе. Недвижимость в Пензе. Провести коммуникации в Пензе. Построить коттедж в Пензе. Перепланировка квартиры в Пензе. Оформление документации в Пензе. Строительство в Пензе.'
DEFAULT_KEYWORDS = 'согласования, разрешения, Пенза, penzact, межевание, оформление, проект, дом, коттедж, коммуникации, земля, участок, квартира, перепланировка, недвижимость, помещение, строительство, в пензе'

def static_view(filename):
    return bottle.static_file(
            filename,
            root=bottle.request.environ['app.STATIC_DIR'],
            )

def favicon_view():
    bottle.redirect(bottle.request.environ['app.FAVICON'])

def liveinternet_reminder_view():
    bottle.response.content_type = 'text/plain;charset=utf-8'
    return 'polymorphm@gmail.com'

def create_app(root=None, static_root=None):
    assert root is not None
    assert static_root is not None
    
    template_lookup = mako_lookup.TemplateLookup(directories=(TEMPLATES_DIR, ))
    
    def init_settings():
        bottle.request.environ.update({
                'app.ROOT': root,
                'app.STATIC_ROOT': static_root,
                })
        
        bottle.request.environ.update({
                'app.STATIC_DIR': STATIC_DIR,
                'app.TEMPLATES_DIR': TEMPLATES_DIR,
                'app.template_lookup': template_lookup,
                'app.DEFAULT_TITLE': DEFAULT_TITLE,
                'app.DEFAULT_DESCRIPTION': DEFAULT_DESCRIPTION,
                'app.DEFAULT_KEYWORDS': DEFAULT_KEYWORDS,
                'app.FAVICON': '{}/favicon.png'.format(bottle.request.environ['app.STATIC_ROOT']),
                })
    
    app = bottle.Bottle()
    
    app.add_hook('before_request', init_settings)
    
    app.route('{}/<filename:path>'.format(static_root), callback=static_view)
    app.route('{}/favicon.ico'.format(root), callback=favicon_view)
    simple_page_views.add_routes(app, root)
    app.route('{}/live-54bc3c7b.txt'.format(root), callback=liveinternet_reminder_view)
    paypal_experiment_views.add_routes(app, root)
    
    return app
