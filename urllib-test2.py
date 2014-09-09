import urllib2
req = urllib2.Request('http://www.baidu.com')
the_page = urllib2.urlopen(req).read()
print the_page
