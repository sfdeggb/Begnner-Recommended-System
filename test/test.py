import pandas 
import numpy 
import xlrd 
import xlutils 
import xlwt 
import re 
import codecs 
import chardet

# path2="E://desktop/huawei表格.xls"
# data=xlrd.open_workbook(path2)
# table=data.sheet_by_index(0)

# def handle_show(show):
#     tem_li=show.split("\n") 
    
#     daxiao=per=reo=ups=""
#     per="none"
#     # if "尺寸" not in tem_li:
#     #     daxiao="none"
#     # if "屏占比" not in tem_li:
#     #     per="none"
#     # if "分辨率"not in tem_li:
#     #     reo="none"
#     try:
#         daxiao=tem_li[tem_li.index("尺寸")+1]
#         reo=tem_li[tem_li.index("分辨率")+1]
#         try:
#             ups=tem_li[tem_li.index("OLED")+1]
#         except Exception as e :
#             ups=tem_li[tem_li.index("类型")+1]
#         finally:
#             pass 
#     except Exception as e:
#         daxiao="none"
#         reo="none"
#     return daxiao,per,reo,ups


# a,b,c,d=handle_show(table.row_values(1)[5])
# print(a)
# print(b)
# print(c)
# print(d)

pattern1=re.compile("[0-9]*0* 万")
pattern2=re.compile("[0-9]*V/[0-9]*A")
pattern3=re.compile("[0-9]+")
pd=pattern2.search("支持 SUPERVOOCTM ")
print(pd)
