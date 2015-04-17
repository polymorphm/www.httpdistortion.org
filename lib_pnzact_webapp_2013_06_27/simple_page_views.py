# -*- mode: python; coding: utf-8 -*-

assert str is not bytes

import bottle
from . import layout

def home_view():
    return layout.render_layout(
            menu_name='home',
            content_file='home.mako',
            )

def private_view():
    return layout.render_layout(
            title='Частным лицам',
            menu_name='private',
            content_file='private.mako',
            )

def enterprise_view():
    return layout.render_layout(
            title='Юр лицам',
            menu_name='enterprise',
            content_file='enterprise.mako',
            )

def our_clients_view():
    return layout.render_layout(
            title='Наши клиенты',
            menu_name='our_clients',
            content_file='our_clients.mako',
            )

def contacts_view():
    return layout.render_layout(
            title='Наши контакты',
            menu_name='contacts',
            content_file='contacts.mako',
            )

def add_routes(app, root):
    app.route(root, callback=home_view)
    app.route('{}/'.format(root), callback=home_view)
    app.route('{}/private'.format(root), callback=private_view)
    app.route('{}/enterprise'.format(root), callback=enterprise_view)
    app.route('{}/our-clients'.format(root), callback=our_clients_view)
    app.route('{}/contacts'.format(root), callback=contacts_view)
