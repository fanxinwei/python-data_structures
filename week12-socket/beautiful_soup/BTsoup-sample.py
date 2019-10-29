# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = 'http://py4e-data.dr-chuck.net/comments_42.html'
url = 'http://py4e-data.dr-chuck.net/comments_52979.html'
# url = input('http://py4e-data.dr-chuck.net/comments_42.html')
# html = urlopen(url, context=ctx).read()
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
sum = 0
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    # print('TAG:', tag)
    # print('URL:', tag.get('href', None))
    # print(tag.get('href', None))
    score = int(tag.contents[0])
    # print(test)
    # print(type(test))
    sum = sum + score
    # print('Contents:', tag.contents[0])
    # print('Attrs:', tag.attrs)
print('the sum is: ', sum)
