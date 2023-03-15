import requests_html as re_h 
from requests_html import HTMLSession
import re 
import xlrd 
import xlwt 
import xlutils 


"xiedejiaoxun\
xiao mi zhe ge wang zhan yong css shi he shi de !\
    bushi suoyou de wang zhan dou shi he xpath"
    
session=HTMLSession()

class xiaohua():
    #类变量
	urls_phone=[]
	urls_param_page=[]
	data=[]
	error_link=[]
	error_recoder=[]
	
	#实例方法
	def __init__(self, base_url, headers=None, cookie=None):
		self.base_url=base_url
		self.headers=headers
		self.cookie=cookie
    
	def get_phons_link_xioami(self):
     #直接人为构造-----名称
		print("*"*25)
		print("正在获取所有小米手机商品链接")
		baseurl="https://www.mi.com/"
		url_list=[]
		names=["redmi-12c","redminote12pro","redminote12pro-plus","redmi-k60",
           "redmi-k60-pro","mi12","xiaomi-13-pro","xiaomi-13","redmi-note-12-pro+",
           "redmi-note-12-pro","redmi-note-12-5g","xiaomi-12s","redminote11",
           "xiaomi-civi-2","xiaomimixflod-2","mi12s-ultra","mi12pro-dimensity",
           "note11t-pro","edminote11t-pro","redmi10a","redmi9a","redmik50","redmik50g"]
		for name in names:
			baseurl=baseurl+names
			url_list.append(baseurl)
		i=0
		for item_url in url_list:
			r=session.get(item_url)
			if (r.status_code != 200):
				self.error_link.append(url)
				print(url+"失败")
				i+=1;
		print("商品连接共{0}条失败".format(i))
		return url_list

	def get_param_link_xiaomi(self,urls):
		#直接人为构造-----
		print("*"*25)
		print("正在获取所有小米手机商品详情的链接")
		for url in urls:
			try:
				self.urls_param_page.append(url+"/specs")
			except Exception as e:
				print("获取参数链接异常！{0}".format(url))
		print("获取所有小米手机商品参数链接完毕")
		return self.urls_param_page

	def get_data_xiaomi(self, urls):
		#什么叫异步请求，ajax属于是异步请求
		print("*"*25)
		print("获取所有小米手机商品数据")
		data=[]
		tem_data=[]
		i=0
		for url in urls:
			#这里可能会发生异常
			print("站在获取第{0}条,地址为{1}".format(i,url))
			try:#所有的都采用css选择器
				r=session.get(url)
				#这里要进行js渲染，大神真的是太牛了
				r.html.render(timeout=30,sleep=1)
				#0
				name=r.html.xpath(
        			"//*[@id='app']/div[2]/div[1]/div[1]/div/div/h2", 
					first=True)
				if(name==None):
					tem_data.append("none")
				else:
					tem_data.append(name.text)
				#1
				######################3
				color=r.html.xpath(
        "//*[@id='app']/div[2]/div[2]/div/div[1]/div[1]/div[2]/div",
						first=True)
				if(color==None):
					tem_data.append("none")
				else:
					tem_data.append(color.text)
				#2
				try:
					img=r.html.xpath(
         "//*[@id='app']/div[2]/div[2]/div/div[1]/div[1]/div[2]/img",
                      first=True)
					if(img==None):
						img=r.html.xpath(
          "//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/img",
                      		first=True)
					img=img.attrs["src"]
					tem_data.append(img)
				except Exception as e:
					tem_data.append("none")
				###################################
				#3
				try:
					h_w_w=r.html.xpath(
         "//*[@id='app']/div[2]/div[2]/div/div[2]/div[1]/div[2]/span",
									first=True)
					if(h_w_w==None):
						h_w_w=r.html.xpath(
          "//*[@id='app']/div[2]/div[2]/div/div[2]/div[2]/div[2]/span",
									first=True)
					h_w_w=h_w_w.text
					tem_data.append(h_w_w)
				except Exception as e:
					tem_data.append("none")
				#4
				plt=r.html.xpath(
        "//*[@id='app']/div[2]/div[2]/div/div[3]/div[1]/div[2]/span",
								first=True)
				if(plt==None):
					tem_data.append("none")
				else:
					tem_data.append(plt.text)
				#5
				mem=r.html.xpath(
        "//*[@id='app']/div[2]/div[2]/div/div[4]/div[1]/div[2]/span",
						first=True)
				if(mem==None):
					tem_data.append("none")
				else:
					tem_data.append(mem.text)				
				#6
				show=r.html.xpath(
        "//*[@id='app']/div[2]/div[2]/div/div[5]/div[1]/div[2]/span",
							first=True)
				if(show==None):
					tem_data.append("none")
				else:
					tem_data.append(show.text)	
				#7
				carmma=r.html.xpath(
        "//*[@id='app']/div[2]/div[2]/div/div[6]/div[4]/span",
							first=True)
				if(carmma==None):
					tem_data.append("none")
				else:
					tem_data.append(carmma.text)	
				#8
				vedio=r.html.xpath(
        "//*[@id='app']/div[2]/div[2]/div/div[6]/div[3]/span",
							first=True)
				if(vedio==None):
					tem_data.append("none")
				else:
					tem_data.append(vedio.text)	
				#9
				power=r.html.xpath(
        "//*[@id='app']/div[2]/div[2]/div/div[7]/div[1]/div[2]/span",
							first=True)
				if(power==None):
					tem_data.append("none")
				else:
					tem_data.append(power.text)	
				data.append(tem_data)#[[........]]
				tem_data=[]
			except Exception as e:
				print("得到详细数据时出现了错误"+url)
				print(e)
				self.error_link.append(url)
				pass
			i+=1
			continue
		return data
	
	def clean_data_xiaomi(self,data_org):#这边使用昨天做的
		#brand	name	color	img	height	wide	weight	
		# mem_cap	ram	rom	mem_size
		# demision	screen_per	recognize	refresh	
		# c_behind	c_front	v_behind	v_front	
        #  platform	cpu	Gpu	
		# power_cap	power_speed
		print("*"*25)
		print("正在清洗所有小米手机商品数据")
		clean_data=[]
		clean_data_sum=[]
		#首先赋值
		for i in range(0,24):
			clean_data.append("none")
		#进行处理,这里貌似可以采用字典
		for record in data_org:
			#这里可能会发生异常
			try:
				clean_data[0]="xiaomi"#brand
				clean_data[1]=record[0]#name
				clean_data[2]=record[1]#color
				clean_data[3]=record[2]#img
				if(len(record[3].split("\n"))==1):
					pass
				else:
					clean_data[4]=record[3].split("\n")[0]#height
					clean_data[5]=record[3].split("\n")[1]#wide
					clean_data[6]=record[3].split("\n")[3]#weight
				if(len(record[5].split("\n"))==1):
					pass
				else:
					clean_data[7]=record[5].split("\n")[0]#men_cap
					clean_data[8]=record[5].split("\n")[3]#ram
					clean_data[9]=record[5].split("\n")[4]#rom
				if(len(record[6].split("\n"))==1):
					pass
				else:
					clean_data[10]="none"#mem_size
					clean_data[11]=record[6].split("\n")[1]#demsion
					clean_data[12]="none"#scree_per
					clean_data[13]=record[6].split("\n")[2]#recogize
					clean_data[14]=record[6].split("\n")[5]#refresh
				if(len(record[7].split("\n"))==1):
					pass
				else:				
					clean_data[15]=record[7].split("\n")[0]#c_behid
					clean_data[16]=record[7].split("\n")[0]#c_front
				if(len(record[8].split("\n"))==1):
					pass
				else:				
					clean_data[17]=record[8].split("\n")[0]#v_behid
					clean_data[18]=record[8].split("\n")[0]#v_font
				if(len(record[4].split("\n"))==1):
					pass
				else:
					clean_data[19]=record[4].split("\n")[0]#plt_form
					clean_data[20]=record[4].split("\n")[2]#cpu
					clean_data[21]=record[4].split("\n")[3]#gpu
				if(len(record[9].split("\n"))==1):
					pass
				else:
					clean_data[22]=record[9].split("\n")[0]#power_cap
					clean_data[23]=record[9].split("\n")[4]+record[9].split("\n")[5]#power_speed 
				clean_data_sum.append(clean_data)
				clean_data=[]
			except Exception:
				print("解析数据时出现了错误！")
				self.error_recoder.append(data_org.index(record))
				pass 
			continue
		print("*"*25)
		print("所有小米手机数据清洗完毕！")	
		return clean_data_sum
   
	def get_phons_link_huawei():
		pass
	def get_param_link_huawei():
		pass 
	def get_data_huawei():
		pass 
	def clean_data_huawei(data_org):
		pass 
	def save_data_all(self,data, option=0):
		print("*"*25)
		print("正在保存所有小米手机数据。。。")
		brands=["xiaomi", "huawei"]
		#create a book
		book = xlwt.Workbook(encoding='utf-8',style_compression=0)
		#create a sheet
		sheet = book.add_sheet(brands[option],cell_overwrite_ok=True)
		#col names
		col = ("brand","name","color","img","height","wide","weight","mem_cap",
			"ram","rom","mem_size","demision" ,"screen_per","recognize","refresh","c_front",
			"c_behind","v_front","v_behind","platform","cpu" ,"Gpu","power_cap","power_speed")
		#write the col names
		for i in range(0,len(col)):
			sheet.write(0,i,col[i])

		for i in range(0,len(data)):
				tem_data = data[i]#[]
				for j in range(0,len(col)):#24
					sheet.write(i+1,j,tem_data[j])
		savepath = "E:/Desktop/"+brands[option]+"表格.xls"
		book.save(savepath)
		print("SHUJU QINGXI WAN BI!!!!")
		
     
if __name__=="__main__":
	urls=["https://www.mi.com/shop/category/list",
          "https://consumer.huawei.com/cn/phones/"]
	user_agent=re_h.user_agent()
	headers={"User-Agent":user_agent}
    # cookie={}
	xiaomi=xiaohua(urls[0], headers=headers)
	# urls=xiaomi.get_phons_link_xioami()
	# urls=xiaomi.get_param_link_xiaomi(urls)
	urls=[
		"https://www.mi.com/xiaomi-13-limited-edition/specs",
		"https://www.mi.com/xiaomi-13-pro/specs",
		"https://www.mi.com/xiaomi-13/specs"
	]
	data1=xiaomi.get_data_xiaomi(urls)
	data2=xiaomi.clean_data_xiaomi(data1)
	xiaomi.save_data_all(data2)
	
	f=open("D:/python/links.txt","w",encoding="UTF-8")
	f2=open("D:/python/record.txt","w",encoding="UTF-8")
	for i in xiaomi.error_link:
		print(i,file=f)
	f.close
	for i in xiaomi.error_recoder:
		print(i,file=f)
	f2.close	
	# # huawei=xiaohua(urls[1])
	# urls=xiaomi.get_phons_link_huawei()
	# urls=xiaomi.get_param_link_huawei(urls)
	# data=xiaomi.get_data_huawei(urls)
	# data=xioami.clean_data_huawei(data)
	# xiaomi.save_data_all(data,option=2)
 
 