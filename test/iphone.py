import requests_html as req 
import re 

session = req.HTMLSession()

domain=["www.vivo.com"]
base_urls=["https://www.vivo.com.cn/products-x.html",
           "https://www.vivo.com.cn/products-s.html",
           "https://www.vivo.com.cn/products-t.html",
           "https://www.vivo.com.cn/products-y.html",
           "https://www.vivo.com.cn/products-iqoo.html"]

headers={}

##
r1=session.get(base_urls[0])
links=r1.html.links
links2=r1.html.absolute_links
for i in links:
	print(i)
 
print(links2)