# -*- coding:utf -*-
# 唤醒手机

import os
import time

class WakeUpScreen(object):

    location_1 = (295.5, 1338)
    location_2 = (583.5, 1338)
    location_3 = (781.5, 1338)

    def vivo(self):
        wake_cmd = 'adb -s 5761c059 shell input keyevent 26'
        os.popen(wake_cmd)
        time.sleep(2.0)

        swipe_cmd = 'adb -s 5761c059 shell input swipe 1000 1200 1000 100 100'
        os.popen(swipe_cmd)
        time.sleep(1.0)

        cmd_1 = 'adb -s 5761c059 shell input tap %d %d'%(self.location_1[0], self.location_1[1])
        os.popen(cmd_1)
        time.sleep(0.5)

        cmd_2 = 'adb -s 5761c059 shell input tap %d %d' % (self.location_2[0], self.location_2[1])
        os.popen(cmd_2)
        time.sleep(0.5)

        cmd_3 = 'adb -s 5761c059 shell input tap %d %d' % (self.location_3[0], self.location_3[1])
        os.popen(cmd_3)
        time.sleep(0.5)

        cmd_3 = 'adb -s 5761c059 shell input tap %d %d' % (self.location_3[0], self.location_3[1])
        os.popen(cmd_3)
        time.sleep(0.5)

        cmd_2 = 'adb -s 5761c059 shell input tap %d %d' % (self.location_2[0], self.location_2[1])
        os.popen(cmd_2)
        time.sleep(0.5)

        cmd_1 = 'adb -s 5761c059 shell input tap %d %d' % (self.location_1[0], self.location_1[1])
        os.popen(cmd_1)
        time.sleep(0.5)

    def xiaomi(self):
        wake_cmd = 'adb -s d102deb37d13 shell input keyevent 26'
        os.popen(wake_cmd)
        time.sleep(2.0)

        swipe_cmd = 'adb -s d102deb37d13 shell input swipe 360 800 360 100 100'
        os.popen(swipe_cmd)
        time.sleep(1.0)

if __name__ == '__main__':
    WakeUpScreen.xiaomi(WakeUpScreen)
