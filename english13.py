# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 17:06:40 2020

@author: Mahendra
"""
import json

with open('english3.json') as dict_reader_old:
        #print("Dictionary is red..............0")
        #print(json.load(dict_reader))
        #print('......................1')
    oldWords=json.load(dict_reader_old)