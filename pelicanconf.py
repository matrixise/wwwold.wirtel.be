#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import sys

sys.path.insert(0, '.')
AUTHOR = u'Stephane Wirtel'
AUTHOR_EMAIL = 'stephane@wirtel.be'
SITENAME = u'Stephane Wirtel (@matrixise)'
SITEURL = 'http://wirtel.be'
GITHUB_URL = 'http://github.com/matrixise/'
REVERSE_CATEGORY_ORDER = True
DISQUS_SITENAME = "stephane-wirtel-blog"
GOOGLE_ANALYTICS = "UA-22059464-1"

TIMEZONE = 'Europe/Brussels'

DEFAULT_LANG = u'en'
DEFAULT_CATEGORY = u'Home'

# Blogroll
#LINKS =  (
#    ('Imprimerie Oberlander', 'http://www.oberlander.be'),
#    ('Python.org', 'http://python.org')
#)
#
## Social widget
SOCIAL = (
    ('twitter', 'http://twitter.com/matrixise'),
    ('github', 'http://github.com/matrixise')
)

DEFAULT_PAGINATION = 10
TYPOGRIFY = True

#from pelican.plugins import gravatar
from plugins import drafts
from plugins import gist

PLUGINS = [
#    gravatar,
    drafts,
    gist,
]

ARTICLE_URL = 'posts/{lang}/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{lang}/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_LANG_URL = 'posts/{lang}/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_LANG_SAVE_AS = 'posts/{lang}/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
#PAGE_URL = 'pages/{slug}/'
#PAGE_LANG_URL = 'pages/{slug}-{lang}/'

THEME = 'built-texts'
TWITTER_USERNAME = 'matrixise'

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
TAG_FEED_RSS = 'feeds/tag_%s.rss.xml'
