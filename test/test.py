import http.cookiejar
import shutil
import urllib.request
import urllib.parse


class LoginJust:
    def __init__(self, url, url2, header):
        self.url = url
        self.url2 = url2
        self.header = header
        return

    def CreateOpener(self):
        # 实例化cookie对象
        cookie = http.cookiejar.CookieJar()
        # 创建一个cookie处理器
        CookieHandle = urllib.request.HTTPCookieProcessor(cookie)
        # 创建带有cookie的opener
        opener = urllib.request.build_opener(CookieHandle)
        # 传入header
        head = []
        for key, value in self.header.items():
            elem = (key, value)
            head.append(elem)
        opener.open(self.url)
        return opener

    # 获取验证码图片，并保存到本地
    def getImage(self, opener):
        path = "imageCode_1.jpg"
        # 带cookie和header
        img = opener.open(self.url2)
        print(img)
        with open(path, "wb") as f:
            shutil.copyfileobj(img, f)
            # print(os.stat(path).st_size, 'characters copied')
        return


url_home = "http://sso-cuit-edu-cn-s.webvpn.cuit.edu.cn:8118/authserver/login?service=http%3A%2F%2Fjwgl.cuit.edu.cn%2Feams%2F%3Bjsessionid%3DED90CFD02D418FFCABFC2BB5F891C1E2"
url_img = "http://sso-cuit-edu-cn-s.webvpn.cuit.edu.cn:8118/authserver/captcha"
header = {
    "Accept": "*/*",
    'Accept-Encoding': 'gzip, deflate',
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    'Connection': 'keep-alive',
    "Content-Length": "0",
    "Host": "sso-cuit-edu-cn-s.webvpn.cuit.edu.cn:8118",
    "Origin": "http://sso-cuit-edu-cn-s.webvpn.cuit.edu.cn:8118",
    "Referer": "http://sso-cuit-edu-cn-s.webvpn.cuit.edu.cn:8118/authserver/login?service=http%3A%2F%2Fjwgl.cuit.edu.cn%2Feams%2F%3Bjsessionid%3DED90CFD02D418FFCABFC2BB5F891C1E2",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
}
lj = LoginJust(url_home, url_img, header)
opener = lj.CreateOpener()
lj.getImage(opener)
