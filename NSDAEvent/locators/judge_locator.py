# -*- coding:utf-8 -*-
# 裁判报名管理定位器

from selenium.webdriver.common.by import By

class JudgeLocator(object):

    JUDGE_BUTTON = (By.XPATH, '/html/body/div[3]/div[1]/div/div[3]/a/p') #裁判报名管理按钮
    JUDGE_ADD_BUTTON = (By.XPATH, '//*[@id="addReferee"]') #添加临时裁判按钮
    JUDGE_NAME = (By.XPATH, '//*[@id="refereeName"]') #裁判姓名输入框
    JUDGE_PHONE = (By.XPATH, '//*[@id="refereeMobile"]') #裁判手机号输入框
    JUDGE_PROVINCE = (By.XPATH, '//*[@id="provinceId"]') #裁判省份
    JUDGE_CITY = (By.XPATH, '//*[@id="cityId"]') #裁判市
    JUDGE_SCHOOL = (By.XPATH, '//*[@id="schoolId"]') #裁判学校
    JUDGE_CONFIRM_BUTTON = (By.XPATH, '//*[@id="save"]') #确认添加按钮

    #-----------------------裁判姓名/电话/省市学校------------------------
    JUDGE_NAME_LIST = ['裁判A', '裁判B', '裁判C', '裁判D', '裁判E', '裁判F', '裁判G', '裁判H', '裁判I', '裁判J', '裁判K', '裁判L',
                  '裁判M', '裁判N', '裁判O']
    JUDGE_PHONE_LIST = ['15375453950', '15375453951', '15375453952', '15375453953', '15375453954', '15375453955', '15375453956',
                        '15375453957', '15375453958', '15375453959', '15375453907', '15375453917', '15375453927', '15375453937',
                        '15375453947']
    JUDGE_PROVINCE_LIST = ['安徽省', '安徽省', '北京市', '北京市', '江苏省', '江苏省', '上海市', '上海市', '浙江省', '浙江省', '陕西省', '陕西省',
                           '山东省', '山东省', '山东省']
    JUDGE_CITY_LIST = ['合肥市', '合肥市', '朝阳区', '朝阳区', '苏州市', '苏州市', '杨浦区', '杨浦区', '杭州市', '杭州市', '西安市', '西安市',
                       '青岛市', '青岛市', '青岛市']
    JUDGE_SCHOOL_LIST = ['合肥市第一中学', '合肥一六八中学', '朝阳外国语学校', '中国人民大学附属中学朝阳学校', '苏州市第六中学', '苏州外国语学校',
                         '上海理工大学附属中学', '复旦大学附属中学', '杭州外国语学校', '杭州学军中学', '西安中学', '西安市曲江第一中学', '青岛二中',
                         '山东省青岛第五中学', '山东省青岛第一国际学校']
