# -*- coding:utf-8 -*-
__author__ = 'Administrator'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import random
import time
import os
import MySQLdb

def bwd_login():
    '百万点登陆'
    driver = webdriver.Chrome()
    driver.get("http://xxxxxxxxxxxxxxxx/login")
    driver.find_element_by_xpath("html/body/div[1]/div[1]/form/div[2]/div[1]/p/input").clear()
    driver.find_element_by_xpath("html/body/div[1]/div[1]/form/div[2]/div[1]/p/input").send_keys("admin")
    driver.find_element_by_xpath("html/body/div[1]/div[1]/form/div[2]/div[2]/p/input[1]").clear()
    driver.find_element_by_xpath("html/body/div[1]/div[1]/form/div[2]/div[2]/p/input[1]").send_keys("admin123456")
    captcha = raw_input("u请输入验证码>>>")
    driver.find_element_by_xpath("html/body/div[1]/div[1]/form/div[3]/p/input").send_keys(captcha)
    driver.find_element_by_xpath(".//*[@id='submit']").click()
    time.sleep(3)
    return driver

def get_area_info(driver):
    '获取省份、城市信息'
    area_dict = {}
    driver.get("http://xxxxxxxxxxxxxx/yyyyyyyyy/index")
    time.sleep(2)
    driver.find_element_by_xpath(".//*[@id='k-maincontent']/div[3]/div/form/div[1]/div[1]/ul/li[1]").click()
    provinces = driver.find_element_by_xpath(".//*[@id='sf_id']").find_elements_by_xpath(".//option")
    provinces.pop(0)
    i = 1
    for province in provinces:
        province.click()
        time.sleep(3)
        cities = driver.find_element_by_xpath(""
                                              ".//*[@id='sc_id']").find_elements_by_xpath(".//option")
        #cities.pop(0)
        area_dict[i] = len(cities)
        i += 1
    return area_dict

def custom_portal_area(driver, i, j):
    '通过省份、城市来自定义portal'
    driver.find_element_by_xpath(".//*[@id='k-maincontent']/div[3]/div/form/div[1]/div[1]/ul/li[1]").click()
    provinces = driver.find_element_by_xpath(".//*[@id='sf_id']").find_elements_by_xpath(".//option")
    provinces[i].click()
    province_name = provinces[i].text
    time.sleep(2)
    cities = driver.find_element_by_xpath(".//*[@id='sc_id']").find_elements_by_xpath(".//option")
    cities[j].click()
    city_name = cities[j].text
    time.sleep(1)
    main_auth_methods = driver.find_element_by_xpath(".//*[@id='rz_pid']").find_elements_by_xpath(".//option")
    main_auth_methods[random.randint(1, 3)].click()
    if random.randint(0, 1):
        second_auth_methods = driver.find_element_by_xpath(".//*[@id='frz_pid']").find_elements_by_xpath(".//option")
        second_auth_methods[random.randint(1, 3)].click()
    if random.randint(0, 1):
        driver.find_element_by_xpath(".//*[@id='k-maincontent']/div[3]/div/form/div[2]/div[1]/div[4]/div/label[1]/input").click()
    if random.randint(0, 1):
        driver.find_element_by_xpath(".//*[@id='k-maincontent']/div[3]/div/form/div[2]/div[1]/div[4]/div/label[2]/input").click()
    portal_modules = driver.find_element_by_xpath(".//*[@id='tplId']").find_elements_by_xpath(".//option")
    portal_modules[2].click()
    pic_list = os.listdir(u"C:\\Users\\Administrator\\interesting_pic")
    pic = u"C:\\Users\\Administrator\\interesting_pic" + "\\" + random.choice(pic_list)
    while True:
        if int(os.stat(pic).st_size) < 500000:
            driver.find_element_by_xpath(".//*[@id='inputImage']").send_keys(pic)
            break
        else:
            pic = u"C:\\Users\\Administrator\\interesting_pic" + "\\" + random.choice(pic_list)
    button_color = random.randint(1, 33)
    driver.find_element_by_xpath(".//*[@id='tplZdy']/div[3]/div[2]/span").click()
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='tplZdy']/div[3]/div[2]/div/span[%d]" % button_color).click()
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='tplZdy']/div[4]/div[2]/span").click()
    text_color = random.randint(1, 33)
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='tplZdy']/div[4]/div[2]/div/span[%d]" % text_color).click()
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='k-maincontent']/div[3]/div/form/div[4]/button").click()
    time.sleep(3)
    print u"%s %s添加成功" % (province_name, city_name)

def get_parter_no():
    '读取数据库，获取网关ID信息'
    conn = MySQLdb.connect(host='192.168.10.72', port=3309, user='100msh_ad', passwd='123456', db='test')
    curs = conn.cursor()
    curs.execute("SELECT partner_no from wal_partner where partner_no != '';")
    record = curs
    gartner_no_list = []
    for gartner_no in record:
        gartner_no_list.append(gartner_no[0])
    return gartner_no_list

def custom_portal_partner(driver, partner_no):
    '通过网关ID来自定义portal'
    driver.find_element_by_xpath(".//*[@id='k-maincontent']/div[3]/div/form/div[1]/div[1]/ul/li[2]").click()
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='d_delivery_parm1']/div[2]/input").send_keys(partner_no)
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='partner_search']").click()
    time.sleep(1)
    main_auth_methods = driver.find_element_by_xpath(".//*[@id='rz_pid']").find_elements_by_xpath(".//option")
    main_auth_methods[random.randint(1, 3)].click()
    if random.randint(0, 1):
        second_auth_methods = driver.find_element_by_xpath(".//*[@id='frz_pid']").find_elements_by_xpath(".//option")
        second_auth_methods[random.randint(1, 3)].click()
    if random.randint(0, 1):
        driver.find_element_by_xpath(".//*[@id='k-maincontent']/div[3]/div/form/div[2]/div[1]/div[4]/div/label[1]/input").click()
    if random.randint(0, 1):
        driver.find_element_by_xpath(".//*[@id='k-maincontent']/div[3]/div/form/div[2]/div[1]/div[4]/div/label[2]/input").click()
    portal_modules = driver.find_element_by_xpath(".//*[@id='tplId']").find_elements_by_xpath(".//option")
    portal_modules[2].click()
    time.sleep(1)
    pic_list = os.listdir(u"C:\\Users\\Administrator\\interesting_pic")
    pic = u"C:\\Users\\Administrator\\interesting_pic" + "\\" + random.choice(pic_list)
    while True:
        if int(os.stat(pic).st_size) < 500000:
            driver.find_element_by_xpath(".//*[@id='inputImage']").send_keys(pic)
            break
        else:
            pic = u"C:\\Users\\Administrator\\interesting_pic" + "\\" + random.choice(pic_list)
    button_color = random.randint(1, 33)
    driver.find_element_by_xpath(".//*[@id='tplZdy']/div[3]/div[2]/span").click()
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='tplZdy']/div[3]/div[2]/div/span[%d]" % button_color).click()
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='tplZdy']/div[4]/div[2]/span").click()
    text_color = random.randint(1, 33)
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='tplZdy']/div[4]/div[2]/div/span[%d]" % text_color).click()
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='k-maincontent']/div[3]/div/form/div[4]/button").click()
    time.sleep(3)
    print u"%s添加成功" % partner_no

def main():
    '主城市'
    driver = bwd_login()
    area_dict = {1: 2, 2: 2, 3: 12, 4: 12, 5: 13, 6: 15, 7: 10, 8: 14, 9: 2, 10: 15, 11: 12, 12: 17, 13: 10, 14: 12, 15: 18, 16: 20, 17: 16, 18: 15, 19: 23, 20: 15, 21: 4, 22: 2, 23: 22, 24: 10, 25: 17, 26: 8, 27: 11, 28: 15, 29: 9, 30: 6, 31: 16, 32: 2, 33: 2, 34: 12, 35: 2}
    # area_dict_2 = {15: 18, 16: 20, 17: 16, 18: 15, 19: 23, 20: 15, 21: 4, 22: 15, 23: 22, 24: 10, 25: 17, 26: 8, 27: 11, 28: 15, 29: 9, 30: 9, 31: 9, 32: 9, 33: 9, 34: 9, 35: 9}
    driver.get("http://d.100m.net/100msh_mopadmin/#wechatRZ/index")
    time.sleep(2)
    i = 0
    num_seen = []
    while i < 500:
        num = random.randint(1000, 9999)
        while True:
            if num not in num_seen:
                num_seen.append(num)
                break
            else:
                num = random.randint(100, 999)
        partner_no = '0101BA29' + str(num)
        try:
            custom_portal_partner(driver, partner_no)
            i += 1
        except Exception, e:
            print e
            driver.get("http://d.100m.net/100msh_mopadmin/#wechatRZ/index")
            time.sleep(2)

    driver.get("http://d.100m.net/100msh_mopadmin/#wechatRZ/index")
    time.sleep(2)
    for i in area_dict.keys():
        for j in range(1, area_dict[i]):
            try:
                custom_portal_area(driver, i, j)
            except Exception, e:
                print e
    time.sleep(5)


if __name__ == "__main__":
    main()
    #print get_parter_no()