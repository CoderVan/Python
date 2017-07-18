#!/usr/bin/python
# -*- coding: UTF-8 -*-


import json

'''
json.dumps	将 Python 对象编码成 JSON 字符串
json.loads	将已编码的 JSON 字符串解码为 Python 对象
'''

data = [{'a' : 1, 'b' : 2,'c' : 3,'c' : 4, 'e' :5}]

# json = json.dumps(data)

# print json

json = json.dumps(data,sort_keys=True,indent=None4,separators=(',',':'))

print json