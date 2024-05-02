# -*- coding: utf-8 -*-
"""CMCC ePortal 登录入口。"""
import eportal

def login(ip, device=0):
    cfg = eportal.load_config(); prof = eportal.profile(cfg); me = cfg["user_info"]
    return eportal.request(prof["base"] + prof["login"].format(
        account=me["account"], password=me["password"], operator="cmcc", ip=ip, device=device))

if __name__ == "__main__":
    print(login(eportal.local_ip()))
 