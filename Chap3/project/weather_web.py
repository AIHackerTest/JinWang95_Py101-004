# !/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask,request,render_template
from API_weather import fetchWeather

app = Flask(__name__)
history = []

@app.route("/", methods=['GET', 'POST'])
def web_weather():
    if request.method == "POST":
        action = request.form.get('action')
        if action == "查询":
            output = fetchWeather(request.form.get('city'))
            if output != "查询失败" and not output in history:
                history.append(output)
            return render_template(
                'index.html',
                output = output)
        elif action == "帮助":
            return render_template(
                'index.html',
                help = True)
        elif action == "历史记录":
            return render_template(
                'index.html',
                history = history)
        else:
            return "未知错误"
    else:
        return render_template('index.html')



if __name__ == "__main__":
    app.run(debug = True)
