# 程序要求：从指定的链接开始，解析html页面，获取所有的herf标签，
# 找到指定位置（position）的链接，
# 重复这个过程指定次数（count)。最终输出找到的人名。

import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = 7
position = 18

name = 'Stanislaw'
for i in range(count):
    url = 'http://py4e-data.dr-chuck.net/known_by_'+ name + '.html'
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    tag_name = tags[position-1]
    name = tag_name.contents[0]
    print('Find name:', name)
