# -*- mode: python; coding: utf-8 -*-

assert str is not bytes

from setuptools import setup

if __name__ == '__main__':
    setup(
            install_requires=(
                    'mysql-connector-python',
                    'bottle',
                    'mako',
                    ),
            )
