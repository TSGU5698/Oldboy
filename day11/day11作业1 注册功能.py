"""
@version:python3
@author:ll
@file:day11作业1 注册功能.py
@time:2022/1/12 15:40
"""
inp_name = input("please input your name:").strip()
inp_password = input("please input your name:").strip()

with open("db.txt",mode="at",encoding="utf-8") as f:
    f.write("{}:{}\n".format(inp_name,inp_password))