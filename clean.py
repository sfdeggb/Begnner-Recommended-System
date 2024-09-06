import re  
import xlrd 
import xlwt 

""" 
oppo官网手机数据清洗与整理
"""
#open the book 
path="E:/desktop/oppo.xls"
wb=xlrd.open_workbook(path)
#find the sheet that doing
sheet=wb.sheet_by_name(sheet_name="oppo")
#rows
sheet.nrows
#split 
cbehind_list=sheet.col_values(colx=15, start_rowx=1)
cfront_list=sheet.col_values(colx=16, start_rowx=1)
powerspeed_list=sheet.col_values(colx=23, start_rowx=1)
# print(cbehind_list[0])
# print(cfront_list[0])
# print(powerspeed_list[0])
#dealing
cbehind=[]
cfront=[]
powerspeed=[]
pattern1=re.compile("[0-9]*0* 万")
pattern2=re.compile("[0-9]*V/[0-9]*A")
pattern3=re.compile("[0-9]+")
i =1
for item in cbehind_list:
	cb=pattern1.search(item)
	if cb==None:
		cbehind.append("none")
	else:
		cbehind.append(cb.group())
	
for item in cfront_list:
	cf=pattern1.search(item)
	if cf==None:
		cfront.append("none")
	else:
		cfront.append(cf.group())
for item in powerspeed_list:
	pd=pattern2.search(item)
	if pd==None:
		powerspeed.append("none")
	else:
		pd_li=pattern3.findall(pd.group())
		if(len(pd_li)!=2):
			powerspeed.append("none")
		else:		
  			powerspeed.append(int(pd_li[0])*int(pd_li[1]))

#save
# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding = 'utf-8')
# 创建一个worksheet
worksheet = workbook.add_sheet('clean_data')
# 写入excel
# 参数对应 行, 列, 值
jj=0
for ii in cbehind:
	worksheet.write(jj,0, ii)
	jj+=1
jj=0
for ii in cfront:
	worksheet.write(jj,1, ii)
	jj+=1
jj=0
for ii in powerspeed:
	worksheet.write(jj,2,ii)
	jj+=1
# 保存
workbook.save('D:/phone/222.xls')
print("wanbi")
