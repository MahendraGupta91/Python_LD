# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 20:15:03 2020

@author: Mahendra
"""
import json
import re
#import re
#with open('english13.text') as English_word_reader:
#    English_word=json.load(English_word_reader)
##    print(len(English_word))
#    
#    
#with open('english13.text') as dict_reader:
#        #print("Dictionary is red..............0")
#        print(len(json.load(dict_reader)))
#        #print('......................1')
#        #oldWords=json.load(dict_reader)
        
f = open("english13.text", "r")
#for i in range(20):
word_text=f.read()
word_text=re.split("\n",word_text)
print(len(word_text))
for i in range(100):
    print(word_text[i].strip(' '))