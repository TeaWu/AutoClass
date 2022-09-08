import http.cookiejar
import urllib.request
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

# 实例化cookie对象
cookie = http.cookiejar.CookieJar()
# 创建一个cookie处理器
CookieHandle = urllib.request.HTTPCookieProcessor(cookie)
print(CookieHandle)
# 创建带有cookie的opener
opener = urllib.request.build_opener(CookieHandle)
opener.open(base_url)
print(cookie)
