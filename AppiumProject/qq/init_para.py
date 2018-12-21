# -*- coding:utf-8 -*-

class InitParm(object):

    device_udid = 'd102deb37d13'
    send_text = '目前最快的赚钱平台，想做的速度下载'
    qun_name_list = ['输了你赢了全世界又如', '下坝小学', '北京CPA考试群', '福利优惠购物群x1477', '室内装修设计交流', '湖南化妆师-新年快乐',
                     '新娘化妆师交流(一)', '杭州化妆师交流群', '山西化妆师交流1群'] #群名称
    index = 1 #调用发送图片的方法
    text = 1 #代表发送文本消息

    desired_caps = {'platformName': 'Android',
                    'platformVersion': '6.0.1',
                    'deviceName': 'xiaomi',
                    'udid': device_udid,
                    'appPackage': 'com.tencent.mobileqq',
                    'appActivity': 'com.tencent.mobileqq.activity.SplashActivity',
                    'unicodeKeyboard': True,
                    'resetKeyboard': True,
                    'noReset': True
                    }