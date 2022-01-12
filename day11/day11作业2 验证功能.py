"""
@version:python3
@author:ll
@file:day11作业2 验证功能.py
@time:2022/1/12 15:45
"""
inp_name = input("please input your name:").strip()
inp_password = input("please input your name:").strip()

with open("db.txt",mode="rt",encoding="utf-8") as f:
    for line in f:
        name,password = line.strip().split(":")
        if inp_name == name and inp_password == password:
            print("login successful")
            break
    else:
        print("login error")