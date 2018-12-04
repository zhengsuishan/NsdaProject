# -*-coding:utf-8 -*-
# 参数

class InitPara(object):

    device_udid = '5761c059'
    add_text = 'text'

    desired_caps = {'platformName': 'Android',
                    'platformVersion': '8.1.0',
                    'deviceName': 'vivo',
                    'udid':device_udid,
                    'appPackage': 'com.tencent.mm',
                    'appActivity': 'com.tencent.mm.ui.LauncherUI',
                    'unicodeKeyboard': True,
                    'resetKeyboard': True,
                    'noReset': True
                    }
    #------------------聊天成员页面--------------------------
    vivo_swipe_time = 500
    vivo_user_swipe_x = 540
    vivo_user_swipe_y1 = 1080
    vivo_user_swipe_y2 = 811
    vivo_user_y = 530.5
    vivo_user_x = 156
    vivo_user_x_dur = 192

    vivo_swipe_top_x = 540
    vivo_swipe_top_y1 = 400
    vivo_swipe_top_y2 = 1080
    vivo_swipe_top_time = 100
