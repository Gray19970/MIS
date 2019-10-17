# -*- coding: utf-8 -*-
# name=Gray_jiang
# version=python3.7
import selenium
from  selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains


def brower_click(brower,list_click):
    list_xy_s = [(59, 72),
                 (125, 72),
                 (200, 72),
                 (260, 72),
                 (59, 142),
                 (125, 142),
                 (200, 142),
                 (260, 142), ]
    picture=brower.find_element_by_id('J-loginImg')
    for i in list_click:
        position=list_xy_s[int(i)-1]
        ActionChains(brower).move_to_element_with_offset(picture,position[0],position[1]).click().perform()
    print('通过了图片验证')
    brower.find_element_by_id('J-login').click()
    print('成功登录')
    return brower
