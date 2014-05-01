bohemian
========

![Screenshot 1](http://omphalosskeptic.github.io/images/bohemian2.png)

### About
[Live Demo — Subtheme 1](http://omphalosskeptic.github.io) // [Live Demo — Subtheme 2](http://scienceclass.github.io)// [Source Code](http://github.com/omphalosskeptic/bohemian)
<br><br>

Bohemian is a pelican theme I wrote to use here on my github page, replacing my older [Clean](http://omphalosskeptic.github.io/clean-pelican-theme.html) theme. It’s **Free, Responsive, Open Source, & Typographically Tasteful**; built to provide a great reading experience with minimal clutter, Bohemian will ready your Pelican site for 21st century.

### Features

- Fully Responsive
- Lightweight
- Two Handsome Subthemes build on the same base … the one on this site and the theme used by [Science Class](http://scienceclass.github.io)
- Handsome webfonts served by [Brick](http://brick.im) for blazing speed, Alegreya for subtheme 1, Playfair Display & Crimson Roman for Subtheme2
- Modern, clutter free design makes for a great reading experience.
- Option to use text or image for the logo
<br>


## Example config:

```
#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Omphalosskeptic' # What shows up as post attribution and site attribution
SITENAME = u'omphalosskeptic' # Main site name
SITE_TITLE = ' — Omphalosskeptic’s Userpage' # Site title, which is appended to site name for the <title?
SITESUBTITLE = 'The Projects <span class="amp">&amp;</span> Thoughts Of Omphalosskeptic' # Shows up at the bottom where no one will notice it. That’s how hip bohmeian is.
SITEURL = 'http://omphalosskeptic.github.io' # Self explanatory
TWITTER_HANDLE = 'omphalosskeptic' # Adds a link to your twitter account in the footer if you have one. Don’t include the @ symbol for this to work

META_DESCRIPTION = "A hub for the open-source projects of web designer & developer Omphalosskeptic." # Goes in the meta description tag. Shows up in google results so don’t forget it.

SITELOGO = SITEURL+'/images/omphalosskeptic_coloured.png' # For subtheme 1, use a square logo 200px +. For subtheme two works best with something about 700px by a few hundred.

USE_CLEAN_SUBTHEME = False # Set this to true and you get a scienceclass.github.io look, alse it’s the theme on omphalosskeptic.github.io

PATH  = 'content'

MENUITEMS = (('Projects', SITEURL+'/category/projects.html'),) # If yo want’t fine grained control over your menu

DEFAULT_CATEGORY = 'Projects'

THEME = 'bohemian' # Important stuff, yo.

TIMEZONE = 'America/Vancouver'

DEFAULT_DATE = 'fs' # Sets the date if you don’t.

# Feed generation is usually not desired when developing

# GITHUB_URL = 'http://github.com/omphalosskeptic'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

```

### Subtheme 1
<img src="http://omphalosskeptic.github.io/images/bohemian1.png" style="width: 100%;max-width:800px;margin: 0 auto;" />
<img src="http://omphalosskeptic.github.io/images/bohemian3.png" style="width: 100%;max-width:800px;margin: 0 auto;" />

### Subtheme 2

<img src="http://omphalosskeptic.github.io/images/bohemian5.png" style="width: 100%;max-width:800px;margin: 0 auto;" />
<img src="http://omphalosskeptic.github.io/images/bohemian6.png" style="width: 100%;max-width:800px;margin: 0 auto;" />
<img src="http://omphalosskeptic.github.io/images/bohemian7.png" style="width: 100%;max-width:800px;margin: 0 auto;" />
