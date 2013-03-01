#!/usr/bin/env python

from apiclient.discovery import build
from optparse import OptionParser

import json
import urllib

# Set DEVELOPER_KEY to the "API key" value from the "Access" tab of the
# Google APIs Console http://code.google.com/apis/console#access
# Please ensure that you have enabled the Youtube Data API and Freebase API
# for your project
DEVELOPER_KEY = 'AIzaSyBX-57s6vyT-6sz5xKJerB-mawR7AhPNZM'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
FREEBASE_SEARCH_URL = 'https://www.googleapis.com/freebase/v1/search?%s'

def get_topic_id(options):
    freebase_params = dict(query=options.query, key=DEVELOPER_KEY)
    freebase_url = FREEBASE_SEARCH_URL % urllib.urlencode(freebase_params)
    freebase_response = json.loads(urllib.urlopen(freebase_url).read())

