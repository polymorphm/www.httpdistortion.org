# -*- mode: python; coding: utf-8 -*-

assert str is not bytes

import bottle

def layout_render(**kwargs):
    assert 'content_file' in kwargs
    
    template = bottle.request.environ['app.template_lookup'].get_template('layout.mako')
    
    tpl_kwargs = {
            'request': bottle.request,
            'title': bottle.request.environ['app.DEFAULT_TITLE'],
            'description': bottle.request.environ['app.DEFAULT_DESCRIPTION'],
            'keywords': bottle.request.environ['app.DEFAULT_KEYWORDS'],
            'download_link_html':
                    '<a '
                    'href="https://www.dropbox.com/s/sw69ff8yhnoo43f/http-distortion-build-12.7z?dl=1" '
                    'target="_blank">http-distortion-build-12.7z</a>',
            'download_last_update':
                    'Sun 20 Mar 2016 23:46:48 MSK',
            }
    tpl_kwargs.update(kwargs)
    
    bottle.response.set_header('Content-Type', 'text/html;charset=utf-8')
    bottle.response.set_header(
            'Content-Security-Policy',
            'frame-ancestors \'self\''
            )
    
    return template.render(**tpl_kwargs)
