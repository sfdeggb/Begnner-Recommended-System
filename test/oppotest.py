from selenium import webdriver 
from selenium.webdriver.common.by import By
import re 
# import page 

options=webdriver.EdgeOptions()
# #some settings 
# #some settings
# options=webdriver.EdgeOptions()

options.set_capability("user-agent",
                       "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.98 Safari/537.36")
#set this task is unviaable
options.add_argument("--headless") 

driver=webdriver.Edge("D:/edgedriver_win64/msedgedriver.exe",options=options)
driver.get("https://www.oppo.com/cn/smartphones/series-find-n/find-n2/specs/")
driver.implicitly_wait(0.5)
elements=driver.find_elements(by=By.CSS_SELECTOR ,value='div.product-params-container-list-item.param-detail-item')
for element in elements:
    print(element.text)
    # print(element.get_attribute("href"))
# driver.close()
driver.close()
driver.quit()
# my_data=["name","color","size_weight","memory","show","Crrmma","vedio","core","power"]
# my_data2=[1,1,2,1,1,2,1,2,3]
# with open("D://oppo_phone.csv", "w") as f:
#     f.writelines(my_data)
#     # f.writelines(my_data2)
#     # f.writelines(lines)


# element = WebDriverWait(driver,10).
# until(
#         EC.presence_of_element_located(
#             (By.ID,"myDynamicElement")
#             )
    
# )   


