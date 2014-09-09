import urllib2
import urllib

data = {}
data['name'] = 'Somebody Here'
data['location'] = 'Northampton'
data['language'] = 'Python'

url_value = urllib.urlencode(data)
print url_value
url = 'http://www.example.com/example.cgi'
full_url = url + '?' + url_value
data = urllib2.urlopen(full_url)   
