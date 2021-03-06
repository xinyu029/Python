# -*-coding:utf-8-*- 
__author__ = "wang"

import json
import os

def user_input(index):
    if index == 1:
        sr = input("请输入backend：")
    elif index == 2:
        sr = input("请输入要新加的记录：")
    elif index == 3:
        sr = input("请输入要删除的记录：")
    else:
        sr = "错误的序号"
    return sr

def gethaproxinfo(backend):
    li = []
    with open("haprox", "r") as file:
        flag = False
        newstr = "backend " + backend
        for line in file:
            if newstr == line.strip():
                flag = True
                continue
            if flag and line.strip().startswith("backend"):
                flag = False
                break
            if flag and line.strip():
                li.append(line)
    return li

def addhaproxinfo(dic):
    try:
        has_backend = False
        title = "backend " + dic['backend']
        record_dict = dic['record']
        content = "        server " + record_dict['server'] + " " + \
                 record_dict['server'] + " weight " + str(record_dict['weight']) + \
            " maxconn " + str(record_dict['maxconn']) + "\n"
        with open("haprox", 'r') as f1, open("haprox_backup", 'w') as f2:
            for line in f1:
                if title == line.strip():
                    has_backend = True
                    f2.write(line)
                    f2.write(content)
                else:
                    f2.write(line)
                if has_backend and line.strip() == content.strip():
                    continue
            if not has_backend:
                f2.write("\n")
                f2.write(title+"\n")
                f2.write(content)
                f2.flush()
    except Exception:
        print("Error!")



if __name__ == '__main__':
    msg = """
输出：
    1、获取ha记录
    2、增加ha记录
    3、删除ha记录
    """
    print(msg)
    num = input("请输入操作序号：")
    if num.isdigit():
        num = int(num)
        st = user_input(num)
        if num == 1:
            ret = gethaproxinfo(st)
            for item in ret:
                print(item.strip())
        elif num == 2:
            dic = json.loads(st)
            addhaproxinfo(dic)
    else:
        print("输入的并非序号.")

