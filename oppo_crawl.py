"""
爬虫应用
实现对淘宝京东天猫网站上oppo商品信息的爬取
@way：调用官方接口
@author:ZHU JIANHAO
@created : 2023-1-4：21:58

"""
"要解决的问题，他每次都是验证---OK "
"js动态数据生成，wc，找不到在哪里-？\
https://g.alicdn.com/kg/??detail-item-recommend/0.0.12/index-min.js"
"这不得行，只有通过，模拟浏览器去实现了"

##############api_name############## 
# item_search 按关键字搜索淘宝商品
# item_get 获得淘宝商品详情
# item_get_pro 获得淘宝商品详情高级版
########## end#######################

###########args############
#q
#id
###########end args###########

############mydata############
# 产品名称: Huawei/华为 DBY-W09，
# 处理器型号: 高通骁龙865，
# CPU主频: 最高达2.84GHz，
# 屏幕尺寸: 10.95英寸，
# 分辨率: 2560×1600
# 存储类型: UFS
# 颜色分类: MatePad 11】 冰霜银 Mate
###########end data#####################

import requests 
import json 
import bs4 
import re 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

word_list=["oppo手机",
           "oppo平板",
           "oppo电脑"]

#采用类的思想进行封装
class goods_spider:
    #class vaiable
    base_url_tao="https://s.taobao.com/"
    base_url_jin="https://www.jd.com/"
    base_url_tian="https://www.tmall.com/"
	
 
    #entray vaiable
    def __init__(self,user_agnet,proxy,keyword):
        self.user_agnet=user_agnet
        self.proxy=proxy
        self.keyword=keyword
     
    def get_data(url_list):
        #verify,mark a request header
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.98 Safari/537.36",
            "cookie":"_samesite_flag_=true;\
             cookie2=153886363f43866476ff6788f70e3be8;\
             t=f86c27a1269fa0683ded87c336b144c4;\
             sgcookie=E100Zad5/DFohfCNvpk+xUFnWxhZT64hBB1ukTuR+2a/0vxi3rjOlMabpb3PQH+6jGZJXiKDzyXboQu+49oM1eRUO0sXw1c/ZLmahft/zElZvdY=;\
             uc3=nk2=F5RDKJJ71jTzng0=&id2=UUpgRK4AeDjovzk8pQ==&vt3=F8dCvjAdU+3b2HWKQoA=&lg2=URm48syIIVrSKA==;\
             lgc=tb648052727; cancelledSubSites=empty;\
             existShop=MTY3MjgzNTA1NA==;\
             uc4=id4=0@U2gqy1/rleN/ymJTgOsRvc56nO3SPFFc&nk4=0@FY4I65grcHfq4CmXH1dVOp7otcaFmA==;\
             tracknick=tb648052727;\
             enc=hqigo3ywLzOaHsLnoDDKtAaOZEpyMwAIJYA6TUVsE+B126nA+uUQvTLTckWTwZ5odXwIma1rixX0uqi4uE+QdJWB5NvrPMTaPahmrfpLA2c=;\
             mt=ci=4_1; thw=cn; v=0;\
             cna=HyETHPOZ+28CAbaWe9eEAHkE;\
             _m_h5_tk=a371ec9c7db2a106cd2f609c608b548d_1672925628534;\
             _m_h5_tk_enc=e79dbac51c327a01d0624a9aee9c94d5;\
             uc1=pas=0&cookie14=UoezTUbTP79MDg==&cookie21=UtASsssme+Bq&cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA==&existShop=false;\
             _tb_token_=e1677b7377347;\
             x5sec=7b22617365727665723b32223a226233333537386131373436613832663366313464323138383033643233343666434b65653335304745495444675a473533636e4247526f504d6a49784d6a4d774d6a51784f5441774d7a73794d4a4368785a37372f2f2f2f2f77464141773d3d227d; l=fBTXxC7PTGcpYIISoOfaFurza77TsIRYnuPzaNbMi9fPODC65RKGW67uqeYBCnhVFsiDR3yt9lR9BeYBqoYwsWRKe5DDwQHmnmOk-Wf..; isg=BJiYPxs3T8zep2NK7aV396hdacYqgfwLe7GZKNKJ6lOGbThXepCJm2nPpKXdx7Tj"
             }
        #setting the configuretion
        options=webdriver.EdgeOptions()
        #..................
        #..................
        #doing a request
        tao_url=url_list[0]
        tian_url=url_list[1]
        #first do tao bao
        for url in tao_url:
            # response=requests.get(url,headers=headers)
            # #parse and get the data that you need
            # soup=bs4.BeautifulSoup(response.text,"html-parser")
            # data=soup.find("div",id="attributes")
            #这里是js生成，怎么处理js代码
            driver=webdriver.Edge("D:/edgedriver_win64/msedgedriver.exe",
                                  options=options)
            oldHandle = driver.window_handles
            
            
        for url in tian_url:
            #deal is different
            pass
        
        
    #get search page all gooods urls   
    def get_urls(init_page=0,page_num=10,protckey="https:"):
        current_page=0
        url_list=[]
        url_tian=[]
        url_tao=[]
        #doing change page
        for current_page in range(0,page_num+1):
            init_page+=current_page*44
            #get the data
            response=requests.get(url+"search?q="+keyword+"&s="+str(init_page))
            if(response.status_code == 200):
                #dong parse, geting all urls
                soup=bs4.BeautifulSoup(response.text,"html.parser")
                for tag in soup.find_all("a"):
                    url=tag['href']
                    #opan duan shi tianmao huanshi taobao wangzhi
                    if (re.find_all("tmall", url)[0])=="tmall":
                        url=protckey+url
                        url_tian.append(url)
                    elif (re.find_all("taobao", url)[0])=="taobao":
                        url=protckey+url
                        url_tao.append(url)
                    else:
                        print("parse url error!")
                url_list.append(url_tian)
                url_list.append(url_tao)  
            else:
                print("some bad thins may happend in geting urls in a page")
                print(response.status_code)
                print("please check in!")
    def clean_data(data,option=1):
     
    def save_data():
        with open(file, "r", encoding="utf-8"):
            

if __name__="__main__":
    