#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests

# 数据由心知天气API提供
def fetchWeather(location):
    result = requests.get(
        'https://api.seniverse.com/v3/weather/now.json',
        params={
            'key': 'kvmig4hl1qfxxunw',
            'location': location,
            'language': 'zh-Hans',
            'unit': 'c'
            },
        timeout=5)
    try:
        result = result.json()
        dict_location = result['results'][0]['location']
        dict_now = result['results'][0]['now']
        last_update = result['results'][0]['last_update']
    except:
        output = "查询失败"
        return output
    weather = dict_now['text']
    temp = dict_now['temperature']
    output = f"{location}：{weather}，{temp}℃"
    return output
