#!/usr/bin/env python3
# -*- mode: python; coding: utf-8 -*-

assert str is not bytes

import httpdistortion_wsgi as _httpdistortion_wsgi
import pnzact_wsgi as _pnzact_wsgi

_application_by_host_dict = {
    'www.httpdistortion.org': _httpdistortion_wsgi.application,
    'www.pnzact.ru': _pnzact_wsgi.application,
}

def application(environ, start_response):
    host = environ.get('HTTP_HOST')
    
    selected_application = _application_by_host_dict.get(host)
    
    if selected_application is None:
        response_body = 'no application for this host'
        
        start_response('404 Not Found', [
            ('Content-Type', 'text/plain;charset=utf-8'),
        ])
        
        yield response_body.encode()
    
    yield from selected_application(environ, start_response)

#
# Below for testing only
#
if __name__ == '__main__':
    from wsgiref import simple_server as _simple_server
    _httpd = _simple_server.make_server('localhost', 8051, application)
    _httpd.serve_forever()
