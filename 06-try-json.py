# Author: Peter
import requests
import json


url = "http://fanyi.baidu.com/basetrans"
query_string = {
    "query": "人生苦短，我用python",
    "from": "zh",
    "to": "en"
}
headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
response = requests.post(url, data=query_string, headers=headers)
# print(response);
# print(response.content.decode())

html_str = response.content.decode()  #json字符串

dict_ret = json.loads(html_str)
print(dict_ret)
print(type(dict_ret))
ret = dict_ret["trans"][0]["dst"]
print("翻译结果是：", ret)
