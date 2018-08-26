# Author: Peter
from lxml import etree
import requests

url ="https://movie.douban.com/chart"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"};

response = requests.get(url,headers=headers)
html_str = response.content.decode()
# print(html_str)

#使用etree处理数据
html = etree.HTML(html_str)

#1、获取所有的电影的url地址
url_list = html.xpath("//div[@class='indent']/div/table//div[@class='pl2']/a/@href")
# print(url_list)

# 2. 所有图片的地址
img_list = html.xpath("//div[@class='indent']/div/table//a[@class='nbg']/img/@src")
# print(img_list)

# 3. 需要吧每部电影组成一个字典，字典中的是电影的数据，比如标题，url，图片地址，评论数，评分
# 思路：
    # 1. 分组
    # 2. 每一组提取数据
ret1 = html.xpath("//div[@class='indent']/div/table")
# print(ret1)
for table in ret1:
    item = {}
    item['title'] = table.xpath(".//div[@class='pl2']/a/text()")[0].replace("/","").strip()
    item['href'] = table.xpath(".//div[@class='pl2']/a/@href")[0]
    item['img']  = table.xpath(".//a[@class='nbg']/img/@src")[0]
    item['comment_num'] = table.xpath(".//span[@class='pl']/text()")[0]
    item['rating_num'] = table.xpath(".//span[@class='rating_nums']/text()")[0]
    print(item)
