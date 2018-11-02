import urllib2

req = urllib2.Request('http://www.python.org/fish.html')
try:
    resp = urllib2.urlopen(req)
except urllib2.HTTPError as e:
    if e.code == 404:
        pass
    else:
        pass
except urllib2.URLError as e:
    pass
else:
    body = resp.read()
