# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 15:48:19 2020

@author: Mahendra
"""
word="lethal"
import requests
from bs4 import BeautifulSoup

URL="https://www.shabdkosh.com/search-dictionary?e=lethal&lc=hi&sl=en&tl=hi"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'lxml')
#print(soup.text)
row=soup.find_all('ol', attrs={"class": "eirol"})

print(len(row))
if len(row)!=0:
    string=row[0].text
    word_meaning=string.strip(' :')
    #message_setter(word_meaning)
    #newWord=word_collector(word,word_meaning)
    #update_Words(newWord)
    print(word_meaning)
else:
        string="Meaning not found!"
        #message_setter(string)