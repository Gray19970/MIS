# -*- coding: utf-8 -*-
# name=Gray_jiang
# version=python3.7
from bs4 import BeautifulSoup
from  selenium import  webdriver
import re
import time
#导入等待对象模块
from  selenium.webdriver.support.wait import WebDriverWait
#导入条件判断模块
from  selenium.webdriver.support import expected_conditions  as EC
#导入查询元素模块
from selenium.webdriver.common.by import  By

def get_pass(brower,name):
    '''

    :param brower: 浏览器对象
    :param name: 购票人
    :return:
    '''
    wait=WebDriverWait(brower,10,0.1)
    element_wait=wait.until(EC.presence_of_all_elements_located((By.ID,'normalPassenger_0')))
    #获得已经登陆的页面
    html=brower.page_source
    soup=BeautifulSoup(html,'lxml')
    name_list=soup.find_all('label',attrs={'style':'cursor: pointer'})
    name_list=[i.get_text() for i in name_list]
    name_choice=soup.find_all('input',attrs={'class':'check'})
    name_choice=[i['id'] for i in name_choice]
    print(name_list)
    print(name_choice)
    name_adcit=dict(zip(name_list,name_choice))
    print(name_adcit)
    for i in name:
        element_click=brower.find_element_by_id(name_adcit[i]).click()
    element_buy=brower.find_element_by_id('submitOrder_id').click()
    wait_buy=WebDriverWait(brower,10,1)
    element_wait_buy=wait_buy.until(EC.presence_of_all_elements_located((By.LINK_TEXT,'确认')))
    time.sleep(5)
    brower.find_element_by_id('qr_submit_id').click()

