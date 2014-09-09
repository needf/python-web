import urllib2
import urllib
url = "http://www.someserver.com/cgi-bin/register.cgi"
user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
value = {'name' : 'WHY' ,
	 'location' : 'SDY' ,
	 'language' : 'Python'}
headers = { 'User-Agent' : user_agent }
data = urllib.urlencode(value)
req = urllib2.Request(url , data , headers)
response = urllib2.urlopen(req)
the_page = response.read()
