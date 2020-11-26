import re
import requests
from .get_cookies import *

# 返回周报专栏的源码
def getzhoubaoHtml(url):
  cookie = {"Cookie": str(get_cookie())}
  html111 = requests.get(url, cookies = cookie)
  html111.encoding = 'utf-8'
  html111 = html111.text
  # print(html111)
  return html111

# 返回周报的链接
def getzhoubao(html111):
  imglist = re.findall(r'(https\:\/\/weibo\.com\/ttarticle\/p\/show.+?class)', html111)
  for html11 in imglist:
    html11 = html11.replace('" class','')
    # print(html11)
    return html11

# 返回周报的源码
def getzhoubaoHtml1(html11):
  cookie = {"Cookie": str(get_cookie())}
  html1 = requests.get(html11, cookies = cookie)
  html1.encoding = 'utf-8'
  html1 = html1.text
  # print(html1)
  return html1

# 字符串格式输出图片链接
def getzhoubaoImg(html1):
  imglist = re.findall(r'(img\-box\=\"img\-box\"\ class\=\"picbox\"\>\<img\ src\=\"https\:\/\/wx.\.sinaimg\.cn\/large.+?\.jpg)', html1)
  for url1 in imglist:
    url1 = url1.replace('img-box="img-box" class="picbox"><img src="','')
    return url1

html111 = str(getzhoubaoHtml("https://weibo.com/a/hot/7583892511954945_1.html"))
html11 = str(getzhoubao(html111))
html1 = str(getzhoubaoHtml1(html11))
print(getzhoubaoImg(html1))
