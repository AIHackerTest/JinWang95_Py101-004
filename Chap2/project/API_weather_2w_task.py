#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests

KEY = 'kvmig4hl1qfxxunw'  # API key
UID = "UE6D2C576B"  # 用户ID
LOCATION = 'shanghai'  # 所查询的位置，可以使用城市拼音、v3 ID、经纬度等
API = 'https://api.seniverse.com/v3/weather/now.json'  # API URL，可替换为其他 URL
UNIT = 'c'  # 单位
LANGUAGE = 'zh-Hans'  # 查询结果的返回语言

def fetchWeather(location):
    result = requests.get(API, params={
        'key': KEY,
        'location': location,
        'language': LANGUAGE,
        'unit': UNIT
    }, timeout=1)
    return result.json()

query_history = list()
print("本程序数据由心知天气API提供")

while True:
    commend = input("请输入指令或需要查询的城市名： ")

    if commend == "help":
        with open('../resource/help.txt') as helpfile:
            print(helpfile.read())
    elif commend == "history":
        print(query_history)
    elif commend == "exit":
        exit(0)
    else:
        try:
            result = fetchWeather(commend)
            dict_location = result['results'][0]['location']
            dict_now = result['results'][0]['now']
            last_update = result['results'][0]['last_update']
        except:
            print("请重新输入！")
            continue
        weather = dict_now['text']
        temp = dict_now['temperature']
        print("%s的天气状况为：%s，气温为%s摄氏度" % (commend,weather,temp))
        query_history.append([commend,weather])
