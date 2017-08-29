import urllib2
from bs4 import BeautifulSoup
html = urllib2.urlopen("http://www.baidu.com")
bsObj = BeautifulSoup(html.read())
print(bsObj.h1)