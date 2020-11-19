import os, hoshino
from nonebot import *
from hoshino import Service, R
from .get_zhoubao_info import *
from .get_xur_info import *
from .get_chall_info import *
from .get_zhu_info import *


#帮助界面
sv = Service("命运2帮助")

help_txt = '''
[周报] 查看命运2周报
[老九] 查看老九位置和装备
[试炼] 查看试炼周报
[蛛王] 查看蛛王商店
[百科] 光尘商店/宝箱怪等链接
'''
@sv.on_fullmatch("原神帮助")
async def help(bot, ev):
    await bot.send(ev, help_txt)

#功能设定
@sv.on_command('周报',aliases=('命运2周报'),only_to_me=False)
async def zhoubao(session: CommandSession):
    img1 = MessageSegment.image(getzhoubaoImg(html1))
    #print(getzhoubaoImg(html))
    msg = '命运2 周报：\n'
    msg = msg + img1
    await session.send(msg)

@sv.on_command('老九',aliases=('仄','九','xur'),only_to_me=False)
async def xur(session: CommandSession):
    img2 = MessageSegment.image(getxurImg(html2))
    #print(getxurImg(html))
    msg = '命运2 仄：\n'
    msg = msg + img2
    await session.send(msg)

@sv.on_command('试炼',aliases=('奥斯里斯试炼'),only_to_me=False)
async def chall(session: CommandSession):
    img3 = MessageSegment.image(getchallImg(html3))
    #print(getchallImg(html))
    msg = '命运2 试炼周报：\n'
    msg = msg + img3
    await session.send(msg)

@sv.on_command('蛛王',aliases=('蛛王商店','猪王'),only_to_me=False)
async def zhu(session: CommandSession):
    img4 = MessageSegment.image(getzhuImg(html4))
    #print(getzhuImg(html))
    msg = '命运2 蛛王：\n'
    msg = msg + img4
    await session.send(msg)

#百科后续打算做成其他形式，但过两天不一定想做了
@sv.on_command('百科',aliases=('命运2百科'),only_to_me=False)
async def baike(session: CommandSession):
    msg = '&#91;CQ:rich,"jumpUrl":"https://api.xiaoheihe.cn/wiki/get_homepage_info_for_app/?wiki_id=1085660&amp;is_share=1",data={"app":"com.tencent.structmsg"&#93;命运2百科","ver":"0.0.0.1","view":"news"}&#93;&#91;分享&#93;命运2百科\n上小黑盒查看更多《命运2》精彩内 容\nhttps://api.xiaoheihe.cn/wiki/get_homepage_info_for_app/?wiki_id=1085660&amp;is_share=1\n来自: 小黑盒'
    await session.send(msg)