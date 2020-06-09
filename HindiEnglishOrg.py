# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 01:09:56 2020

@author: Mahendra
"""
import requests
from bs4 import BeautifulSoup
word="run"
URL="http://hindi-english.org/index.php?inp="+word+"&anz=yes"
page = requests.get(URL)

soup = BeautifulSoup(page.content,"lxml")
#print(soup.text)

div=soup.find_all('div', attrs={"id":"resultitems"})
print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
print(len(div))
#print(div)
a=div[0].find_all('a')
print(len(a))
for l in range( len(a) if len(a)<5 else 10):
    #if l.text=="\n":
        #print("No Text")
   # else :
        print(a[l].text)
