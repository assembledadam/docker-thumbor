import urllib2
import re

def load_sync(path):
    if not re.match(r'^https?', path):
        path = 'http://%s' % path

    headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36' }
    req = urllib2.Request(path, None, headers)
    return urllib2.urlopen(req).read()