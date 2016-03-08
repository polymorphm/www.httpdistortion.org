# -*- mode: python; coding: utf-8 -*-

assert str is not bytes

import os, os.path
import bottle
import json
import socket

STATIC_DIR = os.path.join(os.path.dirname(__file__), 'static')

def static_view(filename):
    return bottle.static_file(
            filename,
            root=bottle.request.environ['app.STATIC_DIR'],
            )

def addrinfo_view():
    host = bottle.request.params.get('host')
    
    if host is None:
        raise bottle.HTTPError(400, 'missing param: host')
        
        return
    
    rv = []
    
    try:
        addrinfo_list = socket.getaddrinfo(
                host,
                None,
                type=socket.SOCK_STREAM,
                )
    except (ValueError, socket.gaierror):
        pass
    else:
        for addr_family, addr_type, addr_proto, addr_canonname, addr_sockaddr in addrinfo_list:
            if addr_family == socket.AF_INET6:
                rv.append(('AF_INET6', addr_sockaddr[0]))
                
                continue
            
            if addr_family == socket.AF_INET:
                rv.append(('AF_INET', addr_sockaddr[0]))
                
                continue
    
    bottle.response.content_type = 'application/json'
    
    return json.dumps(rv)

def create_app(root=None, static_root=None):
    assert root is not None
    assert static_root is not None
    
    def init_settings():
        bottle.request.environ.update({
                'app.ROOT': root,
                'app.STATIC_ROOT': static_root,
                'app.STATIC_DIR': STATIC_DIR,
                })
    
    app = bottle.Bottle()
    
    app.add_hook('before_request', init_settings)
    
    app.route('{}/<filename:path>'.format(static_root), callback=static_view)
    app.route(root, method='POST', callback=addrinfo_view)
    app.route(root, callback=addrinfo_view)
    app.route('{}/'.format(root), method='POST', callback=addrinfo_view)
    app.route('{}/'.format(root), callback=addrinfo_view)
    
    return app
