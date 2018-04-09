#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/9 10:20 
# @Author  : chesian
# @Site    : 
# @File    : apispider.py
# @Software: PyCharm
import codecs
import json
import random

import time
from bs4 import BeautifulSoup
from selenium import webdriver

from user_agent import Agents
import requests


# 获取首页的所有citys
def get_all_cites():

    url = "https://www.aqistudy.cn/historydata/"

    # data=d, cookies=get_cookies(),
    r = requests.post(url, headers={'User-Agent': random.choice(Agents)})

    # 储存 城市名称
    city_names = []
    soup = BeautifulSoup(r.content)
    nodes = soup.find_all("div", class_="all")[0]
    for a in nodes.find_all("a"):
        # print(a)
        # print(a['href'])#查a标签的href值
        city_names.append(a.string)
        # print(a.string)#查a标签的string
    json.dump(city_names, codecs.open("city_name.json", "w","utf8"))


def parse_html():

    city_names =json.load(codecs.open("city_name.json", "r", "utf8"))

    for city_name in city_names:

        content = codecs.open(u"aqidata/" +city_name  +".html", "r", "utf8").read()
        # print content
        soup = BeautifulSoup(content)
        for a in soup.select("tr"):
            row = ",".join(a.stripped_strings)
            # codecs.open(u"csv/" + city_name + ".csv", "a", "gbk").write(row+"\n")
            row = ",".join([city_name,row])
            codecs.open(u"all.csv", "a", "gbk").write(row+"\n")




def get_aqi():

    city_names =json.load(codecs.open("city_name.json", "r", "utf8"))

    driver = webdriver.Chrome(executable_path="D:\python\jar\chromedriver.exe")

    for city_name in city_names:
        url = "https://www.aqistudy.cn/historydata/monthdata.php?city=%s" % city_name
        # url = "http://datacenter.mep.gov.cn/websjzx/dataproduct/resourceproduct/queryAirDataToReport.vm?cityname=%E5%8C%97%E4%BA%AC%E5%B8%82&citytime=2018-04-0910:00:00&citycode=110000"
        driver.get(url)
        time.sleep(10)
        content=driver.find_element_by_xpath("//table").get_attribute('innerHTML')
        print content
        codecs.open("aqidata/" + city_name + ".html", "w","utf8").write(content)




if __name__ == '__main__':


    # 1、 获取首页的所有citys
    # get_all_cites()

    city_names =json.load(codecs.open("city_name.json", "r", "utf8"))
    print len(city_names)

    # 2、 获取citys的按月 api

    # get_aqi()


    # 3、 解析html到csv

    parse_html()