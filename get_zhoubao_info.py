import re
import urllib.request

def getzhoubaoHtml(url):
  html1 = urllib.request.urlopen(url).read()
  return html1
def getzhoubaoImg(html1):
  #正则表达式目前能用，不能用了再优化
  imglist = re.findall(r'(https\:\/\/cdn\.max\-c\.com\/heybox\/dailynews\/img\/(?!c4f5035d1b8053c400c72c0656c12d97).+?\.jpg)', html1)
  for url1 in imglist:
    return url1
html1 = str(getzhoubaoHtml("https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9441772&wiki_id=1085660&is_share=1"))
#print(getzhoubaoImg(html1))
