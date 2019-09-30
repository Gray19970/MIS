import requests
import lxml.html
etree =lxml.html.etree
from bs4 import  BeautifulSoup
def ip_addr():
    url_login='http://ip.jiangxianli.com/?page=1'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    get_html=requests.get(url_login,headers=headers)
    html=get_html.text
    element=etree.HTML(html)
    ip_text=element.xpath('/html/body/div[1]/div/div[1]/div[2]/table/tbody/tr/td[2]/text()')
    port_text=element.xpath('/html/body/div[1]/div/div[1]/div[2]/table/tbody/tr/td[3]/text()')
    ip_addr=zip(ip_text,port_text)
    ipaddr_list=[]
    for i  in  ip_addr:
        ipaddr_list.append({'http':i[0]+':'+i[1]})
    return  ipaddr_list
if __name__ == '__main__':
    print(ip_addr())
