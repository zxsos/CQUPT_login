# 顶号提速:先用别人一个"在线且能 ping 通"的 IP 占住账号会话(50M 挂在首认证上),
# 再用自己的 true_ip 重认证走"漫游换绑"分支,不重新下限速 -> 落回约 1000M。
import random, socket, time, requests, yaml
from ping3 import ping
cfg = yaml.safe_load(open("config.yaml", encoding="utf-8"))
prof = cfg["profiles"]["CQU"]; me = cfg["user_info"]
def live_ip(base):
    a, b, *_ = base.split(".")
    while True:
        c = f"{a}.{b}.{random.randint(0,255)}.{random.randint(0,255)}"
        print(".", end="", flush=True)
        if ping(c, timeout=1):
            return c
def hit(tmpl, ip, device=None):
    u = prof["base"] + tmpl.format(account=me["account"], password=me["password"],
                                  ip=ip, device=device if device is not None else me["device"])
    print(requests.get(u).text[:80])
if __name__ == "__main__":
    true_ip = socket.gethostbyname(socket.gethostname())
    bait = live_ip(true_ip); print("诱饵IP", bait)
    hit(prof["login"], bait, 1)          # 占住
    time.sleep(3)
    hit(prof["unbind"], true_ip); hit(prof["logout"], true_ip)  # 解绑
    time.sleep(3)
    hit(prof["login"], true_ip, 1)        # 顶号 -> 高带宽
 