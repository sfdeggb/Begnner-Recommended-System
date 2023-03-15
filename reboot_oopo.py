"""
                        oppo 数据采集机器人

function: get the oppo goods information from oppo offical website 
author：zhu jianhao
created: 2023-2-11
notion: this is a origianl program created by me!, if you want to use, 
        please mark the author!!!!!
"""
#################我的思考##################
#该程序可以考虑多线程和多进程来加快速度
#可以考虑采用图像界面来方便用户
#以后有时间了再改改完善一下##########
#####     我遇到的错误
#异常的处理
#粗心大意，有你受的
#可以采用一部分用来测试，不必要每次都重来一边，费事！！！！
#没有图形界面一定要print一些必要信息！！！！
#每次写函数就把注释写上，写好就懒得写了
################end#######################
# coding=utf-8

from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import re 
import sys 
import os 
import xlrd
import xlwt
from xlutils.copy import copy
import time 
import random 

#some settings
options=webdriver.EdgeOptions()

options.set_capability("user-agent",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76")
#set this task is unvisable
options.add_argument("--headless") 
#不要加载css等样式
options.page_load_strategy='eager'

driver=webdriver.Edge("D:/edgedriver_win64/msedgedriver.exe",
                      options=options)

def get_items_url(base_url):
    urls=[]
    #load the driver
    driver.get(base_url)
    driver.implicitly_wait(3) # seconds
    print("正在获取商品链接.......")
    elements=driver.find_elements_by_tag_name("a")
    for element in elements:
        url=element.get_attribute("href")
        urls.append(url)
    print("商品链接数据已经获取完毕！")
    return urls
        
def filter_items_ulr(urls):
    new_urls=[]
    for link in urls:
        if link is None:
            continue
        if re.findall("smartphones", link) and re.findall("series", link):
            new_urls.append(link)
    new_urls=sorted(set(new_urls), key = new_urls.index)
    print("商品链接过滤完毕！")
    return new_urls
            
def get_params_url(urls):
    param_urls=[]
    print("正在解析参数地址！....")
    for link in urls:
        #the window may changed.....
        # driver.forward()
        print("loading..."+link)
        dormancy(1,5)
        driver.get(link)
        driver.implicitly_wait(1) # seconds
        #采用链接文本
        elements=driver.find_elements_by_link_text("参数")
        for element in elements:
            if element.text =="参数":
                 url= element.get_attribute("href")
        #real url
        param_urls.append(url)
    print("参数地址解析完毕！")
    return param_urls
    
def get_data(urls):
    data=[]
    tem_data=[]
    for url in urls:
        try:
            print("正在获取{}的数据".format(url))
            dormancy(1,5)
            driver.get(url)
            #get the data ["name","color","size_weight","memory","show",
            # "Crrmma","vedio","core","power"]
            # driver.find_element_by_class_name("detail-name ft-body-1").text
        
            #进行显示等待
            name= WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "detail-name.ft-body-1"))
                ).text  
            color=driver.find_element_by_class_name("color-list-name.ft-body-3-1").text
            img=driver.find_element_by_xpath(
                "//*[@id='ch-product-param']/div/div/div[1]/div[2]/div[1]/img").get_attribute("src")
            elements=driver.find_elements(by=By.CSS_SELECTOR ,
                value='div.product-params-container-list-item.param-detail-item')
        
            if(len(elements)>=7):
                size_weight="_".join(elements[0].text.split("\n")
                                [1:len(elements[0].text.split("\n"))])  
                memory="_".join(elements[1].text.split("\n")
                            [1:len(elements[1].text.split("\n"))])
                show="_".join(elements[2].text.split("\n")
                        [1:len(elements[2].text.split("\n"))])
                Carmma="_".join(elements[3].text.split("\n")
                            [1:len(elements[3].text.split("\n"))])
                vedio="_".join(elements[4].text.split("\n")
                        [1:len(elements[4].text.split("\n"))])
                core="_".join(elements[5].text.split("\n")
                        [1:len(elements[5].text.split("\n"))])
                power="_".join(elements[6].text.split("\n")
                        [1:len(elements[6].text.split("\n"))])
                tem_data=[name,color,img,size_weight,memory,show,Carmma,vedio,core,power]
            else:
                print("when parse the content somththing is worong")
                print("the name of the phone is"+name+"please check!")
            data.append(tem_data)
            tem_data=[]
        except Exception:
            print("this "+ url+ "may be error, please check!")
            pass 
        continue
    print("数据获取完毕！！！")
    return data 

# 创建Excel数据表并写入表头数据
def write_excel_xls_head(path, sheet_name, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）
    workbook.save(path)  # 保存工作簿
    print("表头写入成功！")
    
# 写入表格数据
def write_excel_xls_append(path, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            new_worksheet.write(i + rows_old, j, value[i][j])  # 追加写入数据，注意是从i+rows_old行开始写入
    new_workbook.save(path)  # 保存工作簿


# 随机休眠
def dormancy(a, b):
    time.sleep(random.randint(a, b))
    
def close_driver():
    driver.close()
    driver.quit()

if __name__=="__main__":
    url_phone="https://www.oppo.com/cn/smartphones/"
    url_ipad="https://www.oppo.com/cn/tablets/"
    url_comp="https://www.oppo.com/cn/headphones/"
    
    book_name_xls = 'D://oppo商品数据2.xls'
    sheet_name_xls = 'oppo数据表'
    my_data=[["name","color","img","size_weight","memory","show","Crrmma","vedio","core","power"], ]
   
    # #获得所有商品链接
    # urls=get_items_url(url_phone)
    # #进行链接的过滤
    # urls=filter_items_ulr(urls)
    # #获得参数链接
    # urls=get_params_url(urls)
    # # 进行数据解析
    data=get_data(["https://www.oppo.com/cn/smartphones/series-k/k10/specs/",
                   "https://www.oppo.com/cn/smartphones/series-k/k10x/specs/",
                   "https://www.oppo.com/cn/smartphones/series-k/k9x/specs/",
                   "https://www.oppo.com/cn/smartphones/series-k/k9s/specs/",
                   "https://www.oppo.com/cn/smartphones/series-k/k9-pro/specs/",
                   "https://www.oppo.com/cn/smartphones/series-k/k9/specs/",
                   "https://www.oppo.com/cn/smartphones/series-k/k7/specs/",
                   "https://www.oppo.com/cn/smartphones/series-k/k7x/specs/",
                   "https://www.oppo.com/cn/smartphones/series-k/k7/specs/",
                   "https://www.oppo.com/cn/smartphones/series-k/k9-pro/specs/",
                   "https://www.oppo.com/cn/smartphones/series-k/k9-pro/specs/",
                   "https://www.oppo.com/cn/smartphones/series-k/reno9-pro/specs/",
                   "https://www.oppo.com/cn/smartphones/series-k/reno9-pro-plus/specs/",
                   "https://www.oppo.com/cn/smartphones/series-k/reno7-se-5g/specs/",
                   "https://www.oppo.com/cn/smartphones/series-reno/reno5-pro-plus/specs",
                   "https://www.oppo.com/cn/smartphones/series-reno/reno4/specs/",
                   ])
    #对数据保存
    write_excel_xls_head(book_name_xls, sheet_name_xls, my_data)
    for record in data:
        tem=[]
        tem.append(record)#[[]]
        write_excel_xls_append(book_name_xls, tem)
    #关闭驱动
    close_driver()
    
    
    