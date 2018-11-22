# -*- coding:utf-8 -*-
# 配置数据：url/登录邮箱/密码/分值区间
class Data(object):

    url = 'http://192.168.48.221:8001' #网站地址
    user_email = '875707618@qq.com' #登录邮箱
    user_password = 'test1234' #登录密码
    implicitly_wait_time = 10 #全局等待时间
    lodding_wait_time = 15 #网络请求等待时间
    wait_time = 3 #非网络请求等待时间
    event_title = '发起赛事 - NSDA' #赛事列表的标题
    event_detail_title = '选手报名管理 - NSDA' #进入赛事页面标题

    #------------------赛事规则设置部分------------------------
    point_low = 20 #分值区间下限
    point_high = 30 #分值区间上限
    DEBATE_ROUND_TIMES = 4 #辩论循环赛轮数


