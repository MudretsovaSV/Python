import urllib2
file=urllib2.urlopen("http://manning.com/data/massage.txt")
message=file.read()
print message
