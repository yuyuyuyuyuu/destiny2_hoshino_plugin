import re
import requests
from .get_cookies import *

# 返回小黑盒的源码
def getxurHtml(url):
  cookie = {"Cookie": str(get_cookie())}
  html222 = requests.get(url, cookies = cookie)
  html222.encoding = 'utf-8'
  html222 = html222.text
  # print(html222)
  return html222

# 返回仄的链接
def getxur(html222):
  imglist = re.findall(r'(https\:\/\/weibo\.com\/ttarticle\/p\/show.+?suda)', html222)
  for html22 in imglist:
    html22 = html22.replace('" suda','')
    # print(html22)
    return html22

# 返回仄的源码
def getxurHtml2(html22):
  cookie = {"Cookie": str(get_cookie())}
  html2 = requests.get(html22, cookies = cookie)
  html2.encoding = 'utf-8'
  html2 = html2.text
  # print(html2)
  return html2

# 字符串格式输出图片链接
def getxurImg(html2):
  imglist = re.findall(r'(img\-box\=\"img\-box\"\ class\=\"picbox\"\>\<img\ src\=\"https\:\/\/wx.\.sinaimg\.cn\/large.+?\.jpg)', html2)
  for url2 in imglist:
    url2 = url2.replace('img-box="img-box" class="picbox"><img src="','')
    return url2

html222 = str(getxurHtml("https://weibo.com/a/hot/7584017452406785_1.html"))
html22 = str(getxur(html222))
html2 = str(getxurHtml2(html22))
print(getxurImg(html2))
