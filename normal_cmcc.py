# -*- coding: utf-8 -*-
"""CMCC ePortal 登录入口。"""
import eportal as ep

if __name__ == "__main__":
    cfg = ep.load_config()
    print(ep.classify(ep.login(ep.profile(cfg), cfg["user_info"], ep.local_ip())))
 