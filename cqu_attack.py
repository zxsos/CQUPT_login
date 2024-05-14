# -*- coding: utf-8 -*-
"""CQU ePortal 顶号提速入口。原理见 README。"""
import time
import eportal as ep

def main():
    cfg = ep.load_config(); prof = ep.profile(cfg); me = cfg["user_info"]
    true_ip = ep.local_ip()
    bait = ep.live_ip(true_ip); print("\n诱饵IP:", bait)
    ep.login(prof, me, bait, 1); time.sleep(3)
    ep.request(prof["base"] + prof["unbind"].format(account=me["account"], ip=true_ip))
    ep.request(prof["base"] + prof["logout"].format(ip=true_ip)); time.sleep(3)
    print("顶号:", ep.classify(ep.login(prof, me, true_ip, 1)))

if __name__ == "__main__":
    main()
 