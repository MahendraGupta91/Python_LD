# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 03:37:48 2020

@author: Mahendra
"""
import json

with open('jsonwriteJSon.json') as json_file:
    data = json.load(json_file)
    #data1=data['people']
    print(len(data))
    print(data)
    print('.............................................')
    data['5']='Vineet'
    data['1']='Sumit'
    print(data)
with open('jsonwriteJSon.json', 'w') as outfile:
    json.dump(data, outfile)
with open('jsonwriteJSon.json') as json_file:
    data = json.load(json_file)
    #data1=data['people']
    print(len(data))
    print(data)
  

#jsonwriteJSon.json