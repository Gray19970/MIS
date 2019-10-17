# -*- coding: utf-8 -*-
# name=Gray_jiang
# version=python3.7
import json
import os
import time
import datetime
file_path=os.path.abspath('../cites.json')
file_path = os.path.join(file_path)
url_init='https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs='
def url_addr(star,end,data_time):
        with open(file_path,'r') as f:
            a = f.read()
        cites = json.loads(a)
        star=star+','+cites[star]
        end =end+','+cites[end]
        url=url_init+star+'&ts='+end+'&date='+data_time+'&flag=N,N,Y'
        return url

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
if __name__ == '__main__':
    a=url_addr('上海','蚌埠','2019-10-28')
    print(a)