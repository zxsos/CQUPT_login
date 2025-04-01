# CQUPT_Login - 校园网登录工具

[![Windows 下载](https://img.shields.io/badge/Download-Windows-blue?style=for-the-badge&logo=windows)](https://github.com/bangbang-0/CQUPT_login/releases/download/cqupt/cqupt.v2.0-release.exe)

> ✨ **哆点bug**

## 快速开始

### 安装依赖
在运行本工具前，请确保安装所需的依赖库：
```shell
  pip install -r requirements.txt
```
🚀 极速版 [attack_version.py](attack_version.py)

特点：无需网关信息，一键配置
配置指南：
```python
# ====== 用户信息 ======
username = "你的学号"    # 例如: 2020114514
password = "你的密码"    # 例如: 123456
operator = "cmcc"       # 运营商  默认移动cmcc   电信telecom  联通unicom
```

🎛️ 标准版 [normal_Version.py](normal_Version.py)
已废弃⚠️

🏫 重大定制版 [cqu_attack.py](cqu_attack.py)
1. 编辑 config.yaml 文件
2. run：
```Yaml
user_info:
  username: "统一认证账号"
  password: "密码"
```

## 免责声明

本项目仅供学习和研究使用，不得用于非法用途。

## 许可证

本项目使用 [MIT 许可证](LICENSE)。
