# -*- mode: python; coding: utf-8 -*-

assert str is not bytes

import bottle

def render_layout(**kwargs):
    assert 'content_file' in kwargs
    
    template = bottle.request.environ['app.template_lookup'].get_template('layout.mako')
    
    tpl_kwargs = {
            'request': bottle.request,
            'title': bottle.request.environ['app.DEFAULT_TITLE'],
            'description': bottle.request.environ['app.DEFAULT_DESCRIPTION'],
            'keywords': bottle.request.environ['app.DEFAULT_KEYWORDS'],
            'tel': '+7 (8412) 78-62-80',
            }
    tpl_kwargs.update(kwargs)
    
    bottle.response.set_header('Content-Type', 'text/html;charset=utf-8')
    bottle.response.set_header('X-Frame-Options', 'DENY')
    bottle.response.set_header('X-Ua-Compatible', 'IE=edge,chrome=1')
    
    return template.render(**tpl_kwargs)
