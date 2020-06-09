# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 01:09:56 2020

@author: Mahendra
"""
import re
import requests
from bs4 import BeautifulSoup
word="apple"
#URL="http://hindi-english.org/index.php?inp="+word+"&anz=yes"
URL="https://www.english-hindi.net/english-to-hindi-meaning-"+word
page = requests.get(URL)

soup = BeautifulSoup(page.content,"lxml")
#print(soup.text)

div=soup.find_all('div', attrs={"class":"box_wrapper"})
#print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
print(len(div))
#print(div)


#for l in range( 1 if len(a)<6 else 1):
try: 
    a=div[0].find_all('span')
    print(len(a))
    print(a[2].text)
    hindi_meaning=re.split(",",a[2].text.strip(a[2].find('label').text))
    print(len(hindi_meaning))
    for a in hindi_meaning:
        print(a)
    hindi_string=""
    for i in range(len(hindi_meaning) if len(hindi_meaning)<4 else 4):
        hindi_string=hindi_string+hindi_meaning[i]+","
    print(hindi_string.strip(","))
    #print(a[3].text.strip(a[3].find('label').text))
except :
    print("Meaning Not Found")
     
            