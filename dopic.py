import os 
import requests 
import xlrd 

#open the book 
path="E:/desktop/oppo.xls"
wb=xlrd.open_workbook(path)
#find the sheet that doing
sheet=wb.sheet_by_name(sheet_name="oppo")
#split 
table_list=sheet.col_values(colx=3, start_rowx=1)
#download
i=1
down_path="D:/phone/"
for url in table_list:
	try:
		res=requests.get(url)
		f=open(down_path+"图片"+str(i)+".png","wb")
		f.write(res.content)
		f.close()
		i+=1
	except Exception as e:
		print(e)
		print(str(i)+"	"+url)
		i+=1
		pass 
	continue
print("the picture downloaded!!!")