# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 01:09:56 2020

@author: Mahendra
"""
import requests
from bs4 import BeautifulSoup
word="request"
#URL="http://hindi-english.org/index.php?inp="+word+"&anz=yes"
URL="https://www.english-hindi.net/english-to-hindi-meaning-"+word
page = requests.get(URL)

soup = BeautifulSoup(page.content,"lxml")
#print(soup.text)

div=soup.find_all('div', attrs={"class":"box_wrapper"})
print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
print(len(div))
#print(div)
a=div[0].find_all('span')
print(len(a))
for l in range( 1 if len(a)<6 else 1):
        try: 
            print(a[2].text.strip(a[2].find('label').text))
            print(a[3].text.strip(a[3].find('label').text))
            #print("Meaning Not Founf")
        except :
            print("Index Exceeds")
     
            