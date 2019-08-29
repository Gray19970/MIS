# -*- coding: ISO-8859-1 -*-
# name=Gray_jiang
# version=python3.7
import pygal
import requests
import json
import csv
import lxml
from  lxml import  etree
import re
from  bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from collections import Counter
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        "Referer": "https://www.51job.com/"}
jobs_list=[]
data_list=[]
def get_URL(num=''):
        aURL = 'https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,'
        bURL = '.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
        URL=aURL+num+bURL
        return URL

def get_html(URL,headers):
        repon = requests.get(URL, headers=headers)
        a = repon.text.encode('ISO-8859-1')
        html = a.decode('gbk')
        html = etree.HTML(html)
        return html

def get_page(str_k=''):

        fist_page = get_URL('1')
        html = get_html(fist_page, headers)
        a = html.xpath('//*[@id="resultList"]/div[55]/div/div/div/span[1]')
        for i in a :
            str_k+=etree.tostring(i,encoding='utf-8').decode('utf-8')
        pagenum=re.findall('\d+',str_k)         #????
        return pagenum[0]

def get_job(html):
        list_job=[]
        job=html.xpath('//*[@id="resultList"]/div/p/span/a/text()')  #?????
        for i  in job:
            i=re.split('\s+',i)
            list_job.append(i[1])
        return list_job

def get_date(html):

        date=html.xpath('//*[@id="resultList"]/div/span[4]/text()')[1:]
        return  date
def set_csv():
    with open('job_data.csv', 'w', newline='') as f:
        csv_l = csv.writer(f)
        csv_l.writerow(['jobs', 'datas'])

def get_csv(datas):
        with open('job_data.csv','a',newline='') as f:
            csv_l=csv.writer(f)
            csv_l.writerow(datas)

def get_die(list_a=[]):
    dic_num=Counter(list_a)
    x=list(dic_num.keys())
    y=list(dic_num.values())
    hist = pygal.Bar()
    hist.title = "Number of jobs per day"
    hist.x_labels = x
    hist.x_title = "Data"
    hist.y_title = "Number"
    hist.add('Gray', y)
    hist.render_to_file('Number_jobs.svg')
    print('OK!!!!!')


if __name__ == '__main__':

    num=int(get_page())
    set_csv()
    for i in range(1,num+1):

        url =get_URL(str(i))         #??????url
        html=get_html(url,headers)   #??????html
       # get_date(html)               #??????data
        #get_job(html)                #????????
        data_l=get_date(html)
        data_list+=data_l
        for m in zip(get_job(html),data_l):
            get_csv(m)
        print('No.*****************************%dis finshed'%i)
    get_die(data_list)
