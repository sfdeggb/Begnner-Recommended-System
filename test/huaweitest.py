from requests_html import HTMLSession 


session=HTMLSession()

r=session.get("https://consumer.huawei.com/cn/phones/mate50-pro/specs/")
r.html.render(timeout=30, sleep=1)

size_weight=r.html.xpath("//*[@id='x-block1']/div[1]/div[1]/div/div[1]/div/div/div/div/div/ul/li[1]/div/div/div",
                             first=True).text

print(size_weight)