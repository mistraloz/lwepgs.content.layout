# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright © 2013 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
import os
from setuptools import setup, find_packages
from version import get_version

version = get_version()

setup(name='gs.content.layout',
    version=version,
    description="Standard pay layout for  GroupServer pages.",
    long_description=open("README.txt").read() + "\n" +
                      open(os.path.join("docs", "HISTORY.txt")).read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        "Environment :: Web Environment",
        "Framework :: Zope2",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: Zope Public License',
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux"
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
      ],
    keywords='zope, groupserver, page, template',
    author='Michael JasonSmith',
    author_email='mpj17@onlinegroups.net',
    url='http://source.iopen.net/groupserver/gs.content.layout',
    license='ZPL 2.1',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['gs', 'gs.content'],
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'setuptools',
        'zope.browserpage',  # For the <browser:page config.
        'zope.tal',  # For tal: and metal: attributes
        'zope.tales',  # For what goes in the tal: and metal: attributes
        'gs.content.css',  # For the CSS resource
        'gs.content.js.bootstrap[zope]',  # For the Twitter Bootstrap resource
        'gs.content.js.disclosure[zope]',  # For the disclosure resource
        'gs.content.js.jquery.base[zope]',  # For the jQuery resource
        'gs.content.js.loader[zope]',  # For the JS loader resource
        'gs.content.js.required[zope]',  # For the required-widgets JS
        'gs.content.js.submit[zope]',  # For the submit button JS
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,)
