#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os

AUTHOR = 'Lee'
SITENAME = '2016 Matsu'
SITEURL = 'http://pages.mongkonglee.com'


PATH = 'content'

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = 'en'
# Pelican will use the file system timestamp information (mtime) 
DEFAULT_DATE = 'fs'
DEFAULT_CATEGORY = 'misc'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Python', 'http://python.org/'), )

# Social widget
SOCIAL = (('github', 'http://github.com/kmollee'),('Blog', 'http://www.mongkonglee.com/'))
          
DEFAULT_PAGINATION = 10

RELATIVE_URLS = True

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = "pagesmongkongleecom"

#GOOGLE_ANALYTICS = ""

DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')

# 必須絕對目錄或相對於設定檔案所在目錄
PLUGIN_PATHS = ['./../plugin']
PLUGINS = ['liquid_tags.notebook', 'tipue_search']
# 目錄設定相對於 reveal 下的 content 目錄
NOTEBOOK_DIR = 'notebook'

#SEARCH_URL = '/search'
'''
if not os.path.exists('_nb_header.html'):     
    import warnings 
    warnings.warn("_nb_header.html not found.") 
else: 
    EXTRA_HEADER = open('_nb_header.html', encoding="utf-8").read()
'''

