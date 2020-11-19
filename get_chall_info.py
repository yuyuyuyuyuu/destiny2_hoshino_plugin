import re
import urllib.request

def getchallHtml(url):
  html3 = urllib.request.urlopen(url).read()
  return html3
def getchallImg(html3):
  #正则表达式目前能用，不能用了再优化
  imglist = re.findall(r'(https\:\/\/cdn\.max\-c\.com\/heybox\/dailynews\/img\/(?!c4f5035d1b8053c400c72c0656c12d97).+?\.jpg)', html3)
  for url3 in imglist:
    return url3
html3 = str(getchallHtml("https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9428079&wiki_id=1085660&is_share=1"))
#print(getchallImg(html3))