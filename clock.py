import datetime
from hoshino.service import Service
from hoshino import Service, R
from nonebot import *
from .get_zhoubao_info import *
from .get_xur_info import *
from .get_chall_info import *
from .get_zhu_info import *

def get_week_day(date):
    week_day = {
        0: '星期一',
        1: '星期二',
        2: '星期三',
        3: '星期四',
        4: '星期五',
        5: '星期六',
        6: '星期日',
    }
    day = date.weekday()
    return week_day[day]
# print(datetime.date.today(), get_week_day(datetime.date.today()))

msg0 = '现在是'
msg1 = datetime.date.today()
msg2 = get_week_day(datetime.date.today())

msg31 = '\n检测到周报已更新'
msg32 = '\n检测到老九已更新'
msg33 = '\n检测到试炼周报已更新'
msg34 = '\n检测到蛛王商店已更新'

msg41 = '命运2 试炼周报：\n图片作者：seanalpha\n'
msg42 = '命运2 仄：\n图片作者：seanalpha\n'
msg43 = '命运2 试炼周报：\n图片作者：seanalpha\n'
msg44 = '命运2 蛛王：\n图片来源：小黑盒百科\n'

img1 = MessageSegment.image(getzhoubaoImg(html1))
img2 = MessageSegment.image(getxurImg(html2))
img3 = MessageSegment.image(getchallImg(html3))
img4 = MessageSegment.image(getzhuImg(html4))

svzb = Service('zhoubao-reminder', enable_on_default=False, help_='周报更新提醒')
svlj = Service('laojiu-reminder', enable_on_default=False, help_='老九更新提醒')
svsl = Service('shilian-reminder', enable_on_default=False, help_='试炼更新提醒')
svzw = Service('zhuwang-reminder', enable_on_default=False, help_='蛛王更新提醒')

msg51 = msg0 + str(msg1) + str(msg2) + msg31
msg52 = msg0 + str(msg1) + str(msg2) + msg32
msg53 = msg0 + str(msg1) + str(msg2) + msg33
msg54 = msg0 + str(msg1) + str(msg2) + msg34

msg61 = msg41 + str(img1)
msg62 = msg42 + str(img2)
msg63 = msg43 + str(img3)
msg64 = msg44 + str(img4)

@svzb.scheduled_job('cron', hour='03', minute='00')
async def zhoubaoreminder():
    if get_week_day(datetime.date.today()) == '星期三':
        await svzb.broadcast(msg51, 'zhoubao-reminder', 0.2)
        await svzb.broadcast(msg61, 'zhoubao-reminder', 0.2)

@svlj.scheduled_job('cron', hour='03', minute='00')
async def laojiureminder():
    if get_week_day(datetime.date.today()) == '星期六':
        await svlj.broadcast(msg52, 'laojiu-reminder', 0.2)
        await svlj.broadcast(msg62, 'laojiu-reminder', 0.2)

@svsl.scheduled_job('cron', hour='03', minute='00')
async def shilianreminder():
    if get_week_day(datetime.date.today()) == '星期三':
        await svsl.broadcast(msg53, 'shilian-reminder', 0.2)
        await svsl.broadcast(msg63, 'shilian-reminder', 0.2)

@svzw.scheduled_job('cron', hour='03', minute='00')
async def zhuwangreminder():
    await svzw.broadcast(msg54, 'zhuwang-reminder', 0.2)
    await svzw.broadcast(msg64, 'zhuwang-reminder', 0.2)
