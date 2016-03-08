# -*- mode: python; coding: utf-8 -*-

assert str is not bytes

import bottle
from . import layout

def home_view():
    return layout.layout_render(
            menu_name='home',
            content_file='home.mako',
            )

def info_view():
    return layout.layout_render(
            title='Дополнительная информация',
            menu_name='info',
            content_file='info.mako',
            )

def download_view():
    return layout.layout_render(
            title='Скачать',
            menu_name='download',
            content_file='download.mako',
            )

def source_view():
    #bottle.redirect('{}/source/overview'.format(bottle.request.environ['app.ROOT']))
    # XXX   see issue https://github.com/bottlepy/bottle/issues/749
    
    bottle.response.status = 303
    bottle.response.set_header(
            'Location',
            '{}/source/overview'.format(bottle.request.environ['app.ROOT']),
            )

def source_render(**kwargs):
    title = kwargs.pop('title', None)
    
    if title is not None:
        title = 'Исходный код / {}'.format(title)
    else:
        title = 'Исходный код'
    
    layout_kwargs = {
            'title': title,
            'menu_name': 'source',
            'child_menu_file': 'source_menu.mako',
            }
    layout_kwargs.update(kwargs)
    
    return layout.layout_render(**layout_kwargs)

def source_overview_view():
    return source_render(
            title='Общая инфомация',
            menu_name='source/overview',
            content_file='source_overview.mako',
            )

def source_howto_view():
    return source_render(
            title='Как собрать и запустить',
            menu_name='source/howto',
            content_file='source_howto.mako',
            )

def add_routes(app, root):
    app.route(root, callback=home_view)
    app.route('{}/'.format(root), callback=home_view)
    app.route('{}/info'.format(root), callback=info_view)
    app.route('{}/download'.format(root), callback=download_view)
    app.route('{}/source'.format(root), callback=source_view)
    app.route('{}/source/overview'.format(root), callback=source_overview_view)
    app.route('{}/source/howto'.format(root), callback=source_howto_view)
