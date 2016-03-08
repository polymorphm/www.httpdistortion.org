#!/usr/bin/env python3
# -*- mode: python; coding: utf-8 -*-

assert str is not bytes

from lib_addrinfo_webapp_2016_03_08 import app as _app_module

application = _app_module.create_app(
        root='/api/addrinfo',
        static_root='/api/addrinfo/static',
        )

#
# Below for testing only
#
if __name__ == '__main__':
    from wsgiref import simple_server as _simple_server
    _httpd = _simple_server.make_server('localhost', 8051, application)
    _httpd.serve_forever()
