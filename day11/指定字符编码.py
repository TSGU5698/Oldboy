"""
@version:python3
@author:ll
@file:指定字符编码.py
@time:2022/1/11 16:09
"""

with open("aaa.txt",mode="rt",encoding="utf-8") as f:
    res = f.read()
    print(res)
