import requests
import lxml.html
etree =lxml.html.etree
from bs4 import  BeautifulSoup
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
def ip_addr():
    url_login='https://www.kuaidaili.com/free/inha/1/'
    get_html=requests.get(url_login,headers=headers)
    html=get_html.text
    element=etree.HTML(html)
    ip_text=element.xpath('//*[@id="list"]/table/tbody/tr/td[1]/text()')
    port_text=element.xpath('//*[@id="list"]/table/tbody/tr/td[2]/text()')
    ip_ad=list(zip(ip_text,port_text))
    list_ipaddr=[]
    for i in ip_ad:
        list_ipaddr.append(i[0]+':'+i[1])
    return list_ipaddr

if __name__ == '__main__':
  print(ip_addr())