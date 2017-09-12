# !/usr/bin/env python3
# -*- coding:utf-8 -*-

weather_dict = dict()
query_history = list()
txt = open('../resource/weather_info.txt','r',encoding = 'utf-8')
count_line = len(txt.readlines())
txt.seek(0)

for i in range(count_line):
    # utf-8文件分为两种，一种带BOM，一种无BOM
    # 如果带BOM,则需要用utf-8-sig解码，以移除开头的BOM,即'\ufeff'
    s = txt.readline().strip('\n').strip('\ufeff')
    slist = s.split(',')
    weather_dict[slist[0]] = slist[1]

"""
以下是教练给出的两种读取文件的方法：
f = open(file)

# 第一种循环方法
line = f.readline()
while line:     # 这样就不需要统计行数，然后使用行数作为循环条件
    print(line)
    line = f.readline()

# 第二种循环方法
for line in f.readlines():
    print(line)

"""


txt.close()

while True:
    name = input("请输入指令或你要查询的城市名： ")
    if name == "help":
        with open('../resource/help.txt') as helpfile:
            print(helpfile.read())
    elif name == "history":
        print(query_history)
    elif name == "exit":
        exit(0)
    elif name in weather_dict:
        weather = weather_dict[name]
        print("%s的天气状况为： %s" % (name,weather))
        query_history.append([name,weather])
    else:
        print("查无此城……")
