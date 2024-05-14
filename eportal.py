# -*- coding: utf-8 -*-
"""ePortal 公共客户端:配置、带超时请求、活IP探测、响应判定。"""
from __future__ import annotations
import random, socket, sys
from typing import Optional
import requests, yaml
from ping3 import ping

TIMEOUT = 10
# 响应特征（ePortal 返回体,脆弱但无更稳信号）
MARKS = {
    "ok": "认证成功",
    "already": '"msg":""',
    "bad_password": "bGRhcCBhdXRoIGVycm9y",   # b64("ldap auth error")
    "inuse": "aW51c2UsIGxvZ2luIGFnYWlu",      # b64("...inuse, login again.")
}

def load_config(path: str = "config.yaml") -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)

def profile(cfg: dict) -> dict:
    return cfg["profiles"][cfg["current_profile"]]

def classify(text: Optional[str]) -> str:
    if not text:
        return "error"
    for k, m in MARKS.items():
        if m in text:
            return k
    return "unknown"

def request(url: str) -> Optional[str]:
    try:
        return requests.get(url, timeout=TIMEOUT).text
    except requests.RequestException as exc:
        print(f"请求失败: {exc}", file=sys.stderr)
        return None

def login(prof, me, ip, device=None):
    return request(prof["base"] + prof["login"].format(
        account=me["account"], password=me["password"], operator=me.get("operator", "cmcc"),
        ip=ip, device=me["device"] if device is None else device))

def live_ip(base: str) -> str:
    a, b, *_ = base.split(".")
    while True:
        cand = f"{a}.{b}.{random.randint(0,255)}.{random.randint(0,255)}"
        print(".", end="", flush=True)
        if ping(cand, timeout=1):
            return cand

def local_ip() -> str:
    return socket.gethostbyname(socket.gethostname())
 