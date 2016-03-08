#!/usr/bin/env python3
# -*- mode: python; coding: utf-8 -*-

assert str is not bytes

from lib_httpdistortion_webapp_2014_04_06 import app as _app_module

application = _app_module.create_app(
        root='',
        static_root='/httpdistortion.static',
        )

#
# Below for testing only
#
if __name__ == '__main__':
    from wsgiref import simple_server as _simple_server
    _httpd = _simple_server.make_server('localhost', 8051, application)
    _httpd.serve_forever()
