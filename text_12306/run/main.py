# -*- coding: utf-8 -*-
# name=Gray_jiang
# version=python3.7
from base64 import b64decode
import json
import time
import datetime
from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains
#导入等待对象模块
from  selenium.webdriver.support.wait import WebDriverWait
#导入条件判断模块
from  selenium.webdriver.support import expected_conditions  as EC
#导入查询元素模块
from selenium.webdriver.common.by import  By
#导入生成目标网址的模块
from text_12306.get_urladdr.get_url import url_addr
from text_12306.choice_train.choice_time import get_user_time
from selenium.webdriver.chrome.options import Options
from text_12306.picure_analysis.picture_xy import get_pic_xy
from text_12306.picure_analysis.click_picture import brower_click
from text_12306.get_passenger.passenger import get_pass

def get_html_12306(url,user_time_list):
    '''
    访问查询的12306网页，获得一个时间班次
    '''
    # chrome_options = Options()
    # chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
    #
    # chrome_options.add_argument('window-size=2560x1440')  # 指定浏览器分辨率
    # chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    # chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
    # # chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    # chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
    # chrome_options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"  # 手动指定使用的浏览器位置
    #
    # brower = webdriver.Chrome(chrome_options=chrome_options)
    brower =webdriver.Chrome()
    brower.get(url)
    wait_time(brower)

    time_list,buy_ticket=get_user_time(user_time_list,brower)
    buy_ticekts(brower, time_list, buy_ticket)
    wait_userid(brower)
    brower.find_element_by_xpath('/html/body/div[32]/div[2]/ul/li[2]/a').click()

    return  brower


def wait_time(brow):
    '''
    设置显性质等待，防止网络问题导致报错
    '''
    start=time.time()
    wait=WebDriverWait(brow,2,0.1)
    element=wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'start-t')))
    print('成功加载到火车班次选择页面用时%.2fs'%(time.time()-start))

def wait_userid(brow):
    start = time.time()
    wait=WebDriverWait(brow,2,0,1)
    element=wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'login-hd-account')))
    print('成功加载到用户登录界面用时%.2fs'%(time.time()-start))

def buy_ticekts(brower,time_list,ticket_xpath):
    '''
    点击预订按钮
    :param brower:  浏览器对象
    :param time_list:
    :param ticket_xpath:
    :return:
    '''
    for i in time_list:
        try:
            need_xpath=ticket_xpath[i]
            need_xpath='//*[@id="'+need_xpath+'"]/td[13]/a'
            brower.find_element_by_xpath('//*[@id="ticket_5l0000G45650"]/td[13]/a').click()
        except Exception:
            continue

def userid_password(brower):
    '''
    输入账号密码
    :param brower:浏览器对象
    :return: 无
    '''
    with open('../password.json') as f:
        password=json.load(f)
    brower.find_element_by_id('J-userName').send_keys(password['id'])
    brower.find_element_by_id('J-password').send_keys(password['password'])
    brower.save_screenshot('./web.png')

picture='../picure_analysis/login.jpg'
def get_picture(brower):
    img_str=brower.find_element_by_xpath('''//*[@id="J-loginImg"]''').get_attribute('src')
    img_str = img_str.split(",")[-1]
    img_str = img_str.replace("%0A", '\n')
    img_data = b64decode(img_str)
    with open(picture, 'wb') as fout:
        fout.write(img_data)
        fout.close()
    brower.find_element_by_id('J-loginImg')



def time_text(data_time):
    '''
    先获得当前时间
    把用户输入的时间进行格式转换
    求出时间差
    和给定的值对比
    :param data_time:
    :return:
    '''
    time_now=datetime.datetime.now()
    data_time=datetime.datetime.strptime(data_time,'%Y-%m-%d')
    time_subtraction=data_time-time_now
    time_vulue=datetime.timedelta(days=29,hours=13,minutes=30)
    if time_subtraction<=time_vulue:
        print('可以开始买票')
        return 1
    else:
        print('还没有到买票时间')
        return 0

def main_def():
    # 获得目标地址
    url = url_addr('上海', '蚌埠', '2019-10-14')
    # 访问该网页
    brower=get_html_12306(url,['10:30','14:05'])
    #输入账号密码
    userid_password(brower)
    #获取验证图片
    get_picture(brower)
    #获得图片分析结果
    list_xy=get_pic_xy(picture)
    print(list_xy)
    #点击验证图片
    brower_click(brower,list_xy)
    get_pass(brower,['蒋中一'])
    time.sleep(10000)
if __name__ == '__main__':
     data_time=input('输入时间用-隔开')
     start_position=input('输入出发地')
     end_position=input('输入终点')
     time_choice=input('输入时间范围的开始')
     time_end = input('输入时间范围的结尾')
     main_def()

