import requests, yaml
cfg = yaml.safe_load(open("config.yaml", encoding="utf-8"))
def login(ip, device=0):
    u = (cfg["base"] + "?c=Portal&a=login&callback=dr1003&login_method=1"
         "&user_account=%2C{device}%2C{account}%40{operator}"
         "&user_password={password}&wlan_user_ip={ip}").format(device=device, ip=ip, **cfg)
    print(requests.get(u).text)
if __name__ == "__main__":
    login("192.168.x.x")
 