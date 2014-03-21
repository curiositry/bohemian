#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Omphalosskeptic'
SITENAME = u'Bohemian'
SITE_TITLE = ' — Bohemian Pelican Theme'
SITESUBTITLE = '* Pelican Theme'
SITEURL = 'localhost/bohemian-theme'

# SITELOGO = 'omphalosskeptic_banner.png'

PATH = 'content'

# MENUITEMS = (('Projects', 'projects.html'),)

DEFAULT_CATEGORY = 'Blog'

THEME = 'bohemian'

PAGE_DIR = 'pages'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

USE_FOLDER_AS_CATEGORY = True
DISPLAY_CATEGORIES_ON_MENU = True

DISPLAY_PAGES_ON_MENU = False

DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
# LINKS =  (('Algebrarules.com', 'http://algebrarules.com/'),
#           ('Automathic.org', 'http://automathic.org/'),
#           ('Emspectrum.info', 'http://emspectrum.info/'),
#           ('Github', 'http://github.com/omphalosskeptic'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'), ('Another social link', '#'),)
          
GITHUB_URL = 'http://github.com/omphalosskeptic'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
