import requests
from lxml import etree
import urllib3

urllib3.disable_warnings()
base_url = "http://sso-cuit-edu-cn-s.webvpn.cuit.edu.cn:8118/authserver/login"
base_headers = {
    "Accept": "*/*",
    'Accept-Encoding': 'gzip, deflate',
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    'Connection': 'keep-alive',
    "Content-Length": "0",
    "Host": "sso-cuit-edu-cn-s.webvpn.cuit.edu.cn:8118",
    "Origin": "http://sso-cuit-edu-cn-s.webvpn.cuit.edu.cn:8118",
    "Referer": "http://sso-cuit-edu-cn-s.webvpn.cuit.edu.cn:8118/authserver/login?service=http%3A%2F%2Fjwgl.cuit.edu"
               ".cn%2Feams%2F%3Bjsessionid%3DED90CFD02D418FFCABFC2BB5F891C1E2",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/105.0.0.0 Safari/537.36",
}

img_url = "http://sso-cuit-edu-cn-s.webvpn.cuit.edu.cn:8118/authserver/captcha"
img_headers = {
    "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "Connection": "keep-alive",
    "Host": "sso-cuit-edu-cn-s.webvpn.cuit.edu.cn:8118",
    "Referer": 'http://sso-cuit-edu-cn-s.webvpn.cuit.edu.cn:8118/authserver/login',
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
# 1.创建session对象
session = requests.session()
pag_text = session.get(url=base_url, headers=base_headers).text

# 2.实例化一个etree对象，方便后面对页面进行数据解析
# tree = etree.HTML(pag_text)

# 3.提取验证码下载地址
# img_path = "https://www.qb5.tw" + tree.xpath('//*[@id="main"]/div[1]/form/fieldset/p[3]/img/@src')[0]
# print(img_path)

# 4.下载验证码,以二进制的方式进行保存
img_content = session.get(img_url, headers=img_headers).content
print(img_content)
with open('./img.png', 'wb') as f:
    f.write(img_content)
print('验证码图片下载成功')

img_code = input('请输入验证码：')

# 5.进行登录，定义post的参数
data = {
    'username': 'test123',
    'password': 'admin@123',
    'checkcode': img_code,
    'usecookie': '315360000',
    'action': 'login',
    'submit': '立即登陆'
}
# 判断是否登录成功
response = session.post(url=base_url, data=data, headers=base_headers, verify=False)
response.encoding = 'gbk'  # 编码防止乱码
response_text = response.text
if "登录成功" in response_text:
    print("登陆成功")
# 请求个人信息页
ge = session.get(url='https://www.qb5.tw/userdetail.php', headers=base_headers, verify=False)
with open('xs.html', 'w', encoding='gbk') as f:
    f.write(ge.text)
