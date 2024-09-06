# import requests_html as re_h 
# from requests_html import HTMLSession
# import re 
# import json 

# session = HTMLSession()


# urls="https://cdn.cnbj1.fds.api.mi-img.com/mi.com-assets/shop/pro/js/product/redmi-k60-pro/specs.7d2d94e0.js"

# headers={
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.98 Safari/537.36",
#     }

# r=session.get("https://www.mi.com/redmi-k60-pro/specs",
#               headers=headers)


# r.html.render(sleep=1)

# # # name=r.html.xpath("//*[@id='app']/div[2]/div[1]/div[1]/div/div/h2", 
# # # 					first=True).text
# # # h_w_w=r.html.xpath("/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/span",
# # #                    first=True).text 
# color=r.html.find(".div11",first=True).text
# print(color)
# # # if(color==None):
# # # 	tem_data.append("none")
# # # else:
# # # 	tem_data.append(color.text)
# # # plt=r.html.xpath("//*[@id='app']/div[2]/div[2]/div/div[3]/div[1]/div[2]/span",
# # # 					first=True).text
# # # mem=r.html.xpath("//*[@id='app']/div[2]/div[2]/div/div[4]/div[1]/div[2]/span",
# # # 			first=True).text
# # # show=r.html.xpath("//*[@id='app']/div[2]/div[2]/div/div[5]/div[1]/div[2]/span",
# # # 			first=True).text 
# # # carmma=r.html.xpath("//*[@id='app']/div[2]/div[2]/div/div[6]/div[4]/span",
# # # 				first=True).text
# # # vedio=r.html.xpath("//*[@id='app']/div[2]/div[2]/div/div[6]/div[3]/span",
# # # 				first=True).text
# # # power=r.html.xpath("//*[@id='app']/div[2]/div[2]/div/div[7]/div[1]/div[2]/span",
# # # 				first=True).text


# # # for i in power.split("\n"):
# # #     print(i)
# # # print(power.split("\n")[4])


# # # def get_phons_link_xioami(base_url):
# # #     url_list=[]
# # #     res=session.get(base_url)
# # #     if (res.status_code==200):
# # #         urls=res.html.links
# # #         print(len(urls))
# # #         for url in urls:
# # #             if re.findall("product_id", url) and int(re.findall("[0-9]+", url)[0])<10000000:
# # #                 url_list.append(url)
# # #     return url_list           
# # # urls=get_phons_link_xioami("https://www.mi.com/shop/category/list") 
# # # print(len(urls))
# # # for i in urls:
# # #     print(i)

# # def get_param_link_xiaomi(urls):
# #     urls_param_page=[]
# #     for url in urls:
# #         res=session.get(url)
# #         res.html.render(timeout=30,sleep=1)
# #         parm_url=res.html.xpath("//*[@id='app']/div[2]/div[1]/div/div/div/div[2]/a[2]",
# #                                 first=True).attrs["href"]
# #         if re.findall("specs", parm_url):
# #             urls_param_page.append(parm_url)
# #     return urls_param_page


# # url=get_param_link_xiaomi(["https://www.mi.com/shop/buy/detail?product_id=18077"])
# # print(url)



# # # def get_data_xiaomi(urls):
# # # 		#什么叫异步请求，ajax属于是异步请求
# # # 		data=[]
# # # 		tem_data=[]
# # # 		error_link=[]
# # # 		for url in urls:
# # # 			#这里可能会发生异常
# # # 			try:
# # # 				r=session.get(url)
# # # 				#这里要进行js渲染，大神真的是太牛了
# # # 				r.html.render(sleep=1)
# # # 				#0
# # # 				name=r.html.xpath("//*[@id='app']/div[2]/div[1]/div[1]/div/div/h2", 
# # # 								first=True)
# # # 				if(name==None):
# # # 					tem_data.append("none")
# # # 				else:
# # # 					tem_data.append(name.text)
# # # 				#1
# # # 				######################3
# # # 				color=r.html.xpath("//*[@id='app']/div[2]/div[2]/div/div[1]/div[1]/div[2]/div",
# # # 						first=True)
# # # 				if(color==None):
# # # 					tem_data.append("none")
# # # 				else:
# # # 					tem_data.append(color.text)
# # # 				#2	
# # # 				img=r.html.xpath("//*[@id='app']/div[2]/div[2]/div/div[1]/img",first=True).attrs["src"]
# # # 				tem_data.append(img)
# # # 				###################################
# # # 				#3
# # # 				try:
# # # 					h_w_w=r.html.xpath("//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/div[2]/span",
# # # 									first=True)
# # # 					if(h_w_w==None):
# # # 						h_w_w=r.html.xpath("//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[2]/span",
# # # 									first=True)
# # # 					h_w_w=h_w_w.text
# # # 					tem_data.append(h_w_w)
# # # 				except Exception as e:
# # # 					tem_data.append("none")
# # # 				#4
# # # 				plt=r.html.xpath("//*[@id='app']/div[2]/div[2]/div/div[3]/div[1]/div[2]/span",
# # # 								first=True)
# # # 				if(plt==None):
# # # 					tem_data.append("none")
# # # 				else:
# # # 					tem_data.append(plt.text)
# # # 				#5
# # # 				mem=r.html.xpath("//*[@id='app']/div[2]/div[2]/div/div[4]/div[1]/div[2]/span",
# # # 						first=True)
# # # 				if(mem==None):
# # # 					tem_data.append("none")
# # # 				else:
# # # 					tem_data.append(mem.text)				
# # # 				#6
# # # 				show=r.html.xpath("//*[@id='app']/div[2]/div[2]/div/div[5]/div[1]/div[2]/span",
# # # 							first=True)
# # # 				if(show==None):
# # # 					tem_data.append("none")
# # # 				else:
# # # 					tem_data.append(show.text)	
# # # 				#7
# # # 				carmma=r.html.xpath("//*[@id='app']/div[2]/div[2]/div/div[6]/div[4]/span",
# # # 							first=True)
# # # 				if(carmma==None):
# # # 					tem_data.append("none")
# # # 				else:
# # # 					tem_data.append(carmma.text)	
# # # 				#8
# # # 				vedio=r.html.xpath("//*[@id='app']/div[2]/div[2]/div/div[6]/div[3]/span",
# # # 							first=True)
# # # 				if(vedio==None):
# # # 					tem_data.append("none")
# # # 				else:
# # # 					tem_data.append(vedio.text)	
# # # 				#9
# # # 				power=r.html.xpath("//*[@id='app']/div[2]/div[2]/div/div[7]/div[1]/div[2]/span",
# # # 							first=True)
# # # 				if(power==None):
# # # 					tem_data.append("none")
# # # 				else:
# # # 					tem_data.append(power.text)	
# # # 				data.append(tem_data)#[[........]]
# # # 			except Exception as e:
# # # 				print("得到详细数据时出现了错误"+url)
# # # 				print(e)
# # # 				error_link.append(url)
# # # 				pass
# # # 			continue
# # # 		return data

# # # data=get_data_xiaomi(["https://www.mi.com/xiaomi-13-limited-edition/specs"])
# # # print(len(data))
# # # print(data)
# # # # for i in data:
# # # #     print(i)



# # clean_data=[]
# # clean_data_sum=[]
# # #首先赋值
# # for i in range(0,24):
# # 	clean_data.append("none")
 
# # print(clean_data)

# print("站在获取第{0}条,地址为{1}....".format(1,"url"))


import json
comments = requests.get('http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-fyfzhac1650783')
comments.encoding = 'utf-8'
print(comments)
jd = json.loads(comments.text.strip('var data=')) #移除改var data=将其变为json数据
