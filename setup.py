# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

version = '0.5'

setup(
    name='ping',
    version=version,
    description="Ping Pong Tournament Organization Tool",
    # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='Ping Pong, Django',
    author='Taller Technologies',
    author_email='maturburu@gmail.com',
    url='http://ping.com.ar',
    package_data={
        'ping' : ['templates/*.html', 'templates/*.*'],
    },
    include_package_data=True,
    zip_safe=False,
    entry_points = {
        'console_scripts': [
            'manage = manage:do_manage',
        ],
    },
    install_requires=[
        "Django",
        "dj-database-url",
        "django-debug-toolbar",
        "south",
        "distribute",
    ],
)
