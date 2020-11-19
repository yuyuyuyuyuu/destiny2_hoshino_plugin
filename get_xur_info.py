import re
import urllib.request

def getxurHtml(url):
  html2 = urllib.request.urlopen(url).read()
  return html2
def getxurImg(html2):
  #正则表达式目前能用，不能用了再优化
  imglist = re.findall(r'(https\:\/\/cdn\.max\-c\.com\/heybox\/dailynews\/img\/(?!c4f5035d1b8053c400c72c0656c12d97).+?\.jpg)', html2)
  for url2 in imglist:
    return url2
html2 = str(getxurHtml("https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9428080&wiki_id=1085660&is_share=1"))
#print(getxurImg(html2))