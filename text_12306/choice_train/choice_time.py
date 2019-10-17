# -*- coding: utf-8 -*-
# name=Gray_jiang
# version=python3.7
from  bs4 import BeautifulSoup
import re
import time
import datetime


def train_time(brower):
    '''
    获得目标的班次列表
    得到符合时间要求的班次车辆对应的订购按钮位置
    //*[@id="ticket_5l0000G10200"]/td[13]/a  预定
    //*[@id="ZE_550000K29012"]  检查有没有票了

      --
    候补
    '''
    soup=BeautifulSoup(brower.page_source,'lxml')
    #获得每个班次的时间
    time_list= [i.get_text()  for i in soup.find_all('strong', class_="start-t") ]
    #获得ticket_5l0000G45650格式的文本，用于后面的匹配
    train_name=soup.find_all('tr',attrs={'id':re.compile('ticket_\w+')})
    #获得G456的文本用于后面的选择高铁还是动车
    train_na=soup.find_all('a',attrs={'title':'点击查看停靠站信息'})
    train_na=[i.get_text() for i in train_na]
    train_na=dict(zip(time_list,train_na))
    train_list=[]
    for i in train_name:
        train_list.append(i['id'])
    train_choice=dict(zip(time_list,train_list))
    remaining_ticket=[a.replace('ticket','ZE') for a in train_list ]
    ticket=dict(zip(time_list,remaining_ticket))
    ticket_lest=[]
    for i in  ticket.values():
        a=soup.find('td',attrs={'id':i})
        ticket_lest.append(a.get_text())
    ticket_lest=dict(zip(time_list,ticket_lest))
    return  time_list,train_choice,ticket,train_na,ticket_lest

def get_user_time(user_time_list,brower):
    '''
    根据用户输入的时间范围把合适的火车挑出来
    :param user_time_list:
    :param brower:
    :return: 时间 如06:05 这样的格式
    '''

    time_list,by_train_ticker,ticket,train_name_list,ticket_lest=train_time(brower)
    time_list=[datetime.datetime.strptime(i,'%H:%M') for i in time_list]
    user_time_list=[datetime.datetime.strptime(i,'%H:%M') for i in user_time_list]
    user_need_time=[]
    for i in time_list:
        if  i>user_time_list[0] and i<user_time_list[1]:
            user_need_time.append(i)
    user_need_time=['{0:0>2}:{1:0>2}'.format(i.hour,i.minute) for i in user_need_time]
    user_need_train_style=get_GK_train('k',user_need_time,train_name_list)
    #返回用户真正需要的火车时间；类型为09:11格式
    for i in user_need_train_style:
        #删除没有票的
        if ticket_lest[i]=='--' and ticket_lest[i]=='候补':
            user_need_train_style.remove(i)
    return user_need_train_style,by_train_ticker

def get_GK_train(user_choice,time_need,adict_time_trainname):
    '''
    :param user_choice: g k t 火车的类型
    :param time_need: 已经筛选出符合要求的时间
    :param adict_time_trainname:  时间和火车名字组成的字典 '06:05': 'G456'
    :return: 返回又符合时间要求又符合火车类型要求的时间'06:05'格式
    '''
    train_style_need=[]
    user_choice=user_choice.upper()
    for i in time_need:
        if  user_choice in adict_time_trainname[i]:
            train_style_need.append(i)
    return train_style_need




