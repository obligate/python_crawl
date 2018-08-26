# Author: Peter
import requests

url = "http://www.baidu.com"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"};
response = requests.get(url,headers=headers)
# print(response)

# 获取网页的html字符串
# response.encoding = "utf-8"
# print(response.text)

print(response.content.decode())