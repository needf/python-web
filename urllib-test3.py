import urllib
import urllib2

url = 'http://www.someserver.com/register.cgi'

value = {'name' : 'MI',
	 'location' : 'china',
	 'sex ':  'Boy' }

data = urllib.urlencode(value)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page




