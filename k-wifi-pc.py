# -*- coding:utf-8 -*-

import urllib
import urllib.request
from bs4 import BeautifulSoup
import re
import random
import time
from urllib.parse import unquote

# 设置目标url，使用urllib.request.Request创建请求
for line in open("target.txt"):
    try:
        url0 = line
        req0 = urllib.request.Request(url0)
        #print(i)
    #
    #     # 使用add_header设置请求头，将代码伪装成浏览器
        req0.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36")
    #
    #     # 使用urllib.request.urlopen打开页面，使用read方法保存html代码
        html0 = urllib.request.urlopen(req0).read()
    #
    #     # 使用BeautifulSoup创建html代码的BeautifulSoup实例，存为soup0
        soup0 = BeautifulSoup(html0,'lxml')
    #
    #     aa = soup0.find_all('div',attrs={"class": "icon-label"})
    #     # for item1 in aa:
    #     #     soup1 = BeautifulSoup(str(item1), 'lxml')
    #     #     aa1 = soup1.find_all("span")
    #     #     ddc = aa1[0].text
    #     #
    #     #     #print(aa1)
    #     #     print(ddc)
    #
    #     for item in aa:
    #         print(item)

    # htmlStr = ""
    # with open("target.txt", "r+", encoding="utf-8") as mm:
    #     htmlStr = mm.read()

    # soup0 = BeautifulSoup(htmlStr, 'lxml')
        aa = soup0.find_all('div', attrs={"class": "icon-label"})


        wifiName, address, email, phone, passwd, number = "", "", "", "", "", ""
        for item in aa:
            # print(item)
            className = item.i["class"][0]
            if className == "pin-icon":
                address = item.span.text.strip()
            elif not address.strip():
                address = "null"

            if className == "wifi-icon":
                wifiName = item.span.text.strip()
            elif not wifiName.strip():
                wifiName = "null"

            if className == "locationdetail-hotspots-icon":
                number = item.span.text.replace("个热点", "").strip()
            elif not number.strip():
                number = "null"

            if className == "phone-icon":
                phone = item.span.text.strip()
            elif not phone.strip():
                phone = "null"

            if className == "mail-icon":
                emailll = item.span.a.span["data-cfemail"]
                email_list = re.findall(r'.{2}', emailll)
                key = email_list[0]
                ll = []
                for e in email_list[1:]:
                    r = hex(int(key, 16) ^ int(e, 16))
                    ll.append(r)
                a = "".join(ll)
                email = unquote(a.replace("0x", "%"))
            elif not email.strip():
                email = "null"

            if className == "cert-icon":
                passwd = item.span.text.strip()
            elif not passwd.strip():
                passwd = "null"

        print(url0.strip()+"======"+address+"======"+wifiName+"======"+number+"======"+phone+"======"+email+"======"+passwd)
        with open("reslt.txt","a+",encoding="utf-8") as f:
            f.write(url0.strip()+"======"+address+"======"+wifiName+"======"+number+"======"+phone+"======"+email+"======"+passwd+"\n")
    except Exception as a:
        pass
    # soup1 = BeautifulSoup(str(item), 'lxml')
    # aa1 = soup1.find_all("span")
    # print(item.span)

    # k_mail = mail[0].text.strip('\n').strip(" ")
    # #print(k_unit)
    # print(k_mail)
    # title = soup1.find_all('p', attrs={"class": "mb-1"})
    # github_link = link[0].text.strip('\n').strip(" ")
#     github_title = title[0].text.strip('\n').strip(" ")
#     pass
#     with open('aa.txt', 'a', encoding="utf8") as file:
#         file.write('https://github.com/'+github_link+'*******'+github_link+'*******'+github_title)
#     print('https://github.com/'+github_link+'*******'+github_link+'*******'+github_title)
