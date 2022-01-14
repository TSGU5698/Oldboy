"""
@version:python3
@author:ll
@file:day11作业3 文件拷贝.py
@time:2022/1/12 16:02
"""

src_file = input("输入源文件地址：").strip()
dst_file = input("输入目的文件地址：").strip()
with open(r"{}".format(src_file),mode="rt",encoding="utf-8") as f1, \
open(r"{}".format(dst_file),mode="wt",encoding="utf-8") as f2:
    # res = f1.read()
    # f2.write(res)
    # 当数据量大的时候不能这么写
    for line in f1:
        f2.write(line)