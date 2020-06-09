import tkinter as tk
import json
from tkinter import Toplevel
import time
import sys
import os
import requests
#from selenium.webdriver.chrome.options import Options
#from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from functools import partial 
from time import strftime
import pyperclip
word="orange"
def hindi_word_web_search(word): 
    #for l in range( 1 if len(a)<6 else 1):
    try:
        URL="https://www.english-hindi.net/english-to-hindi-meaning-"+word
        page = requests.get(URL)
        soup = BeautifulSoup(page.content,"lxml")
        div=soup.find_all('div', attrs={"class":"box_wrapper"})
        #print(len(div))
        a=div[0].find_all('span')
        #for k in range(5):
        #print(a[k])
#        print("Numberof Span")
#        length_span=len(a)
#        print(length_span)
        #print(a[1].find('div'))
        if a[1].find('div')==None:
            hindi_meaning=re.split(",",a[1].text.strip(a[1].find('label').text))
#            print(len(hindi_meaning))
#            for a in hindi_meaning:
#                print(a)
            hindi_string=""
            for i in range(len(hindi_meaning) if len(hindi_meaning)<4 else 4):
                hindi_string=hindi_string+hindi_meaning[i]+","
            hindi_string=hindi_string.strip(",")
            #print(a[3].text.strip(a[3].find('label').text))
            flag=True
        else:
            flag=False
            hindi_string="NA"
    except :
        hindi_string="NA"
        flag=False
    return flag, hindi_string

f,m=hindi_word_web_search(word)
print(f)
print(m)