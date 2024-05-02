# -*- coding: utf-8 -*-
"""ePortal 公共客户端:配置加载、带超时的请求、活IP探测、本地IP枚举。"""
from __future__ import annotations
import random, socket, sys
from typing import Optional
import requests, yaml
from ping3 import ping

TIMEOUT = 10

def load_config(path: str = "config.yaml") -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)

def profile(cfg: dict) -> dict:
    return cfg["profiles"][cfg["current_profile"]]

def request(url: str) -> Optional[str]:
    try:
        return requests.get(url, timeout=TIMEOUT).text
    except requests.RequestException as exc:
        print(f"请求失败: {exc}", file=sys.stderr)
        return None

def live_ip(base: str) -> str:
    """同 /16 内随机探测一个"在线且能 ping 通"的真实 IP 作诱饵。"""
    a, b, *_ = base.split(".")
    while True:
        cand = f"{a}.{b}.{random.randint(0,255)}.{random.randint(0,255)}"
        print(".", end="", flush=True)
        if ping(cand, timeout=1):
            return cand

def local_ip() -> str:
    return socket.gethostbyname(socket.gethostname())
 