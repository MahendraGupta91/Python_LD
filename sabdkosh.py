# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 01:09:56 2020

@author: Mahendra
"""
import requests
from bs4 import BeautifulSoup
word="lethal"
URL="https://www.shabdkosh.com/dictionary/english-hindi/"+word+"/"+word+"-meaning-in-hindi"
page = requests.get(URL)

soup = BeautifulSoup(page.content,"lxml")
print(soup.text)

div=soup.find_all('div', attrs={"class":"col-sm-12"})
print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
print(len(div))
#print(div)
#a=div[0].find_all('li')
#print(len(a))
#for l in range( len(a) if len(a)<5 else 10):
    #if l.text=="\n":
        #print("No Text")
   # else :
#        print(a[l].text)
