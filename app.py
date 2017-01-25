#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/25/17 12:11 PM
# @Author  : Jackling 

cmd_dict = {
    '1': '灯最亮',
    '2': '关灯',
    '3': '灯亮一点',
    '4': '灯暗一点',
    '5': '音量最高',
    '6': '关闭音乐',
    '7': '音量高一点',
    '8': '音量低一点'
}

from flask import Flask
import json
from text_cmd import TextCmdProcessor

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/GetCmd/<text>', methods=['POST', 'GET'])
def trans_cmd(text):
    t = TextCmdProcessor('./data/train.csv')
    res, prob = t.process(text)
    cmd_code = str(res[0])
    cmd_str = cmd_dict[cmd_code]
    res = {'cmd_code': cmd_code, 'cmd': cmd_str}
    return json.dumps(res, ensure_ascii=False)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8006)
