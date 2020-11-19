import re
import urllib.request

def getzhuHtml(url):
  html4 = urllib.request.urlopen(url).read()
  return html4
def getzhuImg(html4):
  #正则表达式目前能用，不能用了再优化
  imglist = re.findall(r'(https\:\/\/cdn\.max\-c\.com\/heybox\/dailynews\/img\/(?!c4f5035d1b8053c400c72c0656c12d97).+?\.png)', html4)
  for url4 in imglist:
    return url4
html4 = str(getzhuHtml("https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=8829978&wiki_id=1085660&is_share=1"))
#print(getzhuImg(html4))