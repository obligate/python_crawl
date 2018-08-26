# Author: Peter
import requests
from retrying import retry

# 专门请求url地址的方法

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
#     }

headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
           "Referer": "https://m.douban.com/tv/american"
}

@retry(stop_max_attempt_number=3)  # 让被装饰的函数反复执行3次，三次全部报错才会报错，中间有一次正常，程序继续往后走
def _parse_url(url):
    print("*" * 100)
    response = requests.get(url, headers=headers, timeout=5)
    return response.content.decode()

def parse_url(url):
    try:
        html_str = _parse_url(url)
    except:
        html_str = None
    return  html_str

if __name__ == '__main__':
    url = "http://www.baidu.com"
    url1 = "www.baidu.com"
    print(parse_url(url1))


