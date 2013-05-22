# -*- coding: utf-8 -*-
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
      "Development Status :: 4 - Beta",
      "Environment :: Web Environment",
      "Framework :: Zope2",
      "Intended Audience :: Developers",
      "License :: Other/Proprietary License",
      "Natural Language :: English",
      "Operating System :: POSIX :: Linux"
      "Programming Language :: Python",
      "Topic :: Software Development :: Libraries :: Python Modules",
      ],
    keywords='zope, groupserver, page, template',
    author='Michael JasonSmith',
    author_email='mpj17@onlinegroups.net',
    url='http://source.iopen.net/groupserver/gs.content.layout',
    license='other',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['gs', 'gs.content'],
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'setuptools',
        'zope.tal',  # For tal: and metal: attributes
        'zope.tales',  # For what goes in the tal: and metal: attributes
        'gs.content.css',  # For the CSS resource
        'gs.content.js.bootstrap',  # For the jquery resource
        'gs.content.js.disclosure',  # For the disclosure resource
        'gs.content.js.jquery',  # For the jquery resource
        'gs.content.js.loader',  # For the JS loader resource
        'gs.content.js.required',  # For the required-widgets JS
        'gs.content.js.submit',  # For the submit button JS
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,)
