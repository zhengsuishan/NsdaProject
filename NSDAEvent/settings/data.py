# -*- coding:utf-8 -*-
# 配置数据：url/登录邮箱/密码/分值区间
class Data(object):

    url = 'http://192.168.48.221:8001/loginOrg/login' #网站地址
    user_email = '875707618@qq.com' #登录邮箱
    user_password = '666888' #登录密码
    implicitly_wait_time = 10 #全局等待时间
    lodding_wait_time = 15 #网络请求等待时间
    wait_time = 3 #非网络请求等待时间
    sleep_time = 1 #UI操作间隔
    event_title = '发起赛事 - NSDA' #赛事列表的标题
    event_detail_title = '选手报名管理 - NSDA' #进入赛事页面标题

    event_type = 1 #赛事类型，1是辩论，2是演讲

    #------------------赛事规则设置部分------------------------
    point_low = 80 #分值区间下限
    point_high = 100 #分值区间上限

    DEBATE_ROUND = 4 #辩论循环赛轮数
    # 设置每轮循环赛匹配规则, 1是随机匹配，2是实力匹配，需要和比赛轮数对应
    MATCH_LIST = [1, 1, 2, 2]
    # 设置每轮循环赛flight, 2是single, 3是double, 4是triple, 需要和比赛轮数对应
    FLISHT_LIST = [2, 3, 4, 2]
    DEBATE_WIN_NUM = 10 #晋级队伍
    SUCCESS_PTOMOTE = '成功临时把比赛时间设为当天' #成功临时把比赛时间设置为今天提示





