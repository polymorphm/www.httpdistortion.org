#!/usr/bin/env python3
# -*- mode: python; coding: utf-8 -*-

assert str is not bytes

from lib_pnzact_webapp_2013_06_27 import app as _app_module

application = _app_module.create_app(
        root='',
        static_root='/static',
        )

#
# Below for testing only
#
if __name__ == '__main__':
    from wsgiref import simple_server as _simple_server
    _httpd = _simple_server.make_server('localhost', 8051, application)
    _httpd.serve_forever()
