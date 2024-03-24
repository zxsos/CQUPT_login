import requests
# 移动 CMCC 版:登录 -> (解绑MAC) -> 登出
BASE = "http://192.168.200.2:801/eportal/"
ACCOUNT, PASSWORD, OPERATOR = "xxxxx", "xxxxx", "cmcc"
ip = "192.168.x.x"
device = 0
def login():
    u = (BASE + "?c=Portal&a=login&callback=dr1003&login_method=1"
         "&user_account=%2C%d%%2C%s%%40%s&user_password=%s&wlan_user_ip=%s"
         % (device, ACCOUNT, OPERATOR, PASSWORD, ip))
    print(requests.get(u).text)
if __name__ == "__main__":
    login()
 