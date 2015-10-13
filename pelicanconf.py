#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jean Guegant'
SITENAME = u"Jean Guegant's Blog"
SITETITLE = AUTHOR
SITESUBTITLE = u'My various personal activities and stories. My passions, my sports, my family, my friends and my fooes.'
SITEURL = 'http://localhost:8000'
SITELOGO = SITEURL + '/images/myself.png'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
            ('Technical/Professional Blog', 'http://jguegant.github.io/blogs/tech/'),
        )

# Menu
USE_FOLDER_AS_CATEGORY = True
MAIN_MENU = True
MENUITEMS = (('Archives', SITEURL + '/archives.html'),
             ('Categories', SITEURL + '/categories.html'),
             ('Tags', SITEURL + '/tags.html'),
             ('Technical/Professional Blog', 'http://jguegant.github.io/blogs/tech/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# THEME
THEME = "../Flex"

# Copyright License.
CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2015
