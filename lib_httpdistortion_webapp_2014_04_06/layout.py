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
                    'href="https://www.dropbox.com/s/g801qwx8jgkdtpc/http-distortion-build-11.7z" '
                    'target="_blank">http-distortion-build-11.7z</a>',
            'download_last_update':
                    'Thu 16 Apr 2015 00:56:17 MSK',
            }
    tpl_kwargs.update(kwargs)
    
    bottle.response.set_header('Content-Type', 'text/html;charset=utf-8')
    bottle.response.set_header(
            'Content-Security-Policy',
            'frame-ancestors \'self\''
            )
    
    return template.render(**tpl_kwargs)
