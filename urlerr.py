import urllib2
req = urllib2.Request('http://www.baidu.com')

try: urllib2.urlopen(req)

except urllib2.URLError,e:
	print e.reason
print 'no error'
