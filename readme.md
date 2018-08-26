##爬虫
### 需要的软件环境
+ python3
+ pycharm
+ chrome

### requests 模块
#### 安装
`pip install requests`
#### 发送get,post请求
- response = requests.get(url) # 发送get请求，请求url地址对应的响应
- response = requests.post(url,data={请求体的字典}) # 发送post请求

#### response的方法
- response.text
  - 该方式往往会出现乱码，出现乱码使用 response.encoding="utf-8"
- response.content.decode() #默认是utf-8编码
  - 把响应的二进制流转化为 str 类型
- reponse.request.url    #发送请求的url地址
- response.url           #response响应的url地址
- response.request.headers #请求头
- response.headers    #响应请求

#### 获取网页源码的正确的打开方式(通过下面三种方式，一定能获取到网页的正确解码之后的字符串)
- 1.response.content.decode()  
- 2.response.content.decode("gbk")
- 3.response.text

#### 发送带 header 的请求
- 为了模拟浏览器，获取和浏览器一模一样的内容
```
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}
response=requests.get(ur,headers=headers)
```
#### 使用超时参数
- requests.get(url,headers=heders,timeout=3) #3秒内必须返回响应，否则会报错

#### retrying模块
- pip install retrying
```python
from retrying import retry
@retry(stop_max_attempt_number=3)
def fun1():
    print("this is func1")
    raise ValueError("this is test error")

```

#### 处理 cookie相关的请求
- 人人网{"email":"mr_mao_hacker@163.com","password":"alarmchime"}
- 直接携带cookie请求的url地址
    - 1.cookie放在headers中
    ```python
      headers={"User-Agent":"...","Cookie":"cookie 字符串"}
    ```
    - 2.cookie字典传给cookies参数
       - requests.get(url,cookies=cookie_dict)
- 先发送post 请求，获取cookie，带上cookie请求登录后的页面
    - 1.session = requests.session() #session具有的方法和requests一样
    - 2.session.post(url,data,headers) #服务器设置在本地的cookie会保存在session
    - 3.session.get(url) # 会带上之前保存的session中的cookie，能够请求成功
    
### 数据提取方法
#### json
- 数据交换格式，看起来像python类型(列表，字典)的字符串
- 使用json之前，需要导入 import json

- 哪里会返回 json 的数据
    - 流程器切换到手机版
    - 抓包app

- json.loads
    - 把json字符串转化为python类型
    -`json.loads(json字符串)`
- json.dumps
    - 把python类型转化为json字符串
    - `json.dumps({"a":"a","b":21})`
    - `json.dumps(ret1,ensure_ascii=False,indent=2)`
        - ensure_ascii 让中文显示成中文
        - indent 能够让下一行在上一行的基础上空格 


### xpath 和 lxml
https://movie.douban.com/chart
https://www.toutiao.com/
- xpath
    - 一门从html中提取数据的语言
- xpath语法
    - xpath helper插件：帮助我们从`elements`中定位数据
    - 1.选择节点（标签）
        - `/html/head/meta`: 能够选中html中的head下的所有的meta标签
    - 2.`//`： 能够从任意节点开始选择
        - `//li` : 当前页面上的所有的li标签
        - `/html/head//link`: head下的所有link标签
    - 3.`@符号的用途`
        - 选择某个具体元素:`//div[@class='feed-infinite-wrapper']/ul/li`
            - 选择class='feed-infinite-wrapper'的div下的ul下的li
        - `a/@href`: 选择a的href的值
    - 4.获取文本
        - `/a/text()` 获取a下面的文本
        - `/a//text()`: 获取a下的所有的文本
    - 5.当前
        - `./a`当前节点下的a标签
```xpath
#https://www.toutiao.com/
//div[@class='feed-infinite-wrapper']/ul/li//div[@class='title-box']/a/@href
//div[@class='feed-infinite-wrapper']/ul/li//div[@class='title-box']/a/text()
#douban https://movie.douban.com/chart
//div[@class='indent']/div/table//div[@class='pl2']//span[@class='rating_nums']/text()
```
- lxml
    - 安装 pip install lxml
    - 使用
    ```python
      from lxml import etree
      element = etree.HTML('html字符串')
      element.xpath("")
    ```
 
###基础知识点
- format ： 字符串格式化的一种方式
```python
"传{}播".format(1)
"传{}播".format([1,2,3])
"传{}播{}".format({1,2,3},[1,2,3])
"传{}播{}".format({1,2,3},1)

```
- 列表推导式
    - 帮助我们快速生成包含一堆数据的列表
    - `[i+10 for i in rang(10)]` -->[10,11,12,...19]
    - `["10月{}日.format(i) for i in range(1,10)]` --> ["10月1日"，"10月2日"，..."10月9日"]
- 字典推导式
    - 帮助我们快速的生成包含一堆数据的字典
```python
{i+10: i for i in range(10)}  => {10:0,11:1,..19:9}
{"a{}".format(i):10 for i in range(3)} => {"a0":10,"a1":10,"a2":10}
```
- 三元运算符
    - if 后面的条件成立，就把if前面的结果赋值给a，否则把else后面的结果赋值给a
```python
a = 10 if 4>3 else 20 #a=10
a = 10 if 4<3 else 20 #a=20

```