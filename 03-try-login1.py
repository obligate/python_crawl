# Author: Peter
import requests

url = "http://www.renren.com/327550029/profile"
headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
           "Cookie": "anonymid=jk81ayae-ay3v1b; depovince=BJ; _r01_=1; JSESSIONID=abc1CnWf5zff17lYOyQtw; ick_login=ecd6d6e7-0858-40a6-b43c-8b5495a883ec; first_login_flag=1; ln_uact=mr_mao_hacker@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn421/20180720/1740/main_JAWQ_0aa000000ceb195a.jpg; loginfrom=syshome; jebe_key=78df4ca1-a89e-4849-9dff-2c2f3072cf7e%7Cc13c37f53bca9e1e7132d4b58ce00fa3%7C1532940701877%7C1%7C1532940707754; wp_fold=0; jebecookies=cc069bf1-2a38-4bc6-a82a-0cb496c03655|||||; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; p=a965cc483114fd8f22fb014071ddd0a99; t=55a2eb629c901008a7c0fdc910283da19; societyguester=55a2eb629c901008a7c0fdc910283da19; id=327550029; xnsid=1597b4f9"}



response = requests.get(url,headers=headers)

with open("renren1.html", "w", encoding="utf-8") as f:
    f.write(response.content.decode())