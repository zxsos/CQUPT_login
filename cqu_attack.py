# -*- coding: utf-8 -*-
"""CQU ePortal 顶号提速入口(基于 eportal 公共客户端)。"""
import time
import eportal

def hit(prof, me, tmpl, ip, device=None):
    return eportal.request(prof["base"] + prof[tmpl].format(
        account=me["account"], password=me["password"], ip=ip,
        device=device if device is not None else me["device"]))

def main():
    cfg = eportal.load_config(); prof = eportal.profile(cfg); me = cfg["user_info"]
    true_ip = eportal.local_ip()
    bait = eportal.live_ip(true_ip); print("\n诱饵IP:", bait)
    hit(prof, me, "login", bait, 1); time.sleep(3)
    hit(prof, me, "unbind", true_ip); hit(prof, me, "logout", true_ip); time.sleep(3)
    print(hit(prof, me, "login", true_ip, 1))   # 顶号 -> 高带宽

if __name__ == "__main__":
    main()
 