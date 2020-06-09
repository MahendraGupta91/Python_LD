# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 01:09:56 2020

@author: Mahendra
"""
import re
import requests
from bs4 import BeautifulSoup
word="chess"
#URL="http://hindi-english.org/index.php?inp="+word+"&anz=yes"



#print(soup.text)


#print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")

#print(div)

def hindi_word_web_search(word): 
    #for l in range( 1 if len(a)<6 else 1):
    try:
        URL="https://www.english-hindi.net/english-to-hindi-meaning-"+word
        page = requests.get(URL)
        soup = BeautifulSoup(page.content,"lxml")
        div=soup.find_all('div', attrs={"class":"box_wrapper"})
        print(len(div))
        a=div[0].find_all('span')
        #for k in range(5):
        #print(a[k])
        print("Numberof Span")
        length_span=len(a)
        print(length_span)
        if length_span>29 :
            hindi_meaning=re.split(",",a[2].text.strip(a[2].find('label').text))
            print(len(hindi_meaning))
            for a in hindi_meaning:
                print(a)
            hindi_string=""
            for i in range(len(hindi_meaning) if len(hindi_meaning)<4 else 4):
                hindi_string=hindi_string+hindi_meaning[i]+","
            hindi_string=hindi_string.strip(",")
            #print(a[3].text.strip(a[3].find('label').text))
            flag=True
        else:
            hindi_string=a[1].text.strip(a[1].find('label').text)
            print(hindi_string)
            flag=True
    except :
        hindi_string="Meaning Not Found"
        flag=False
    return flag, hindi_string


flag,Meaning=hindi_word_web_search("run")
print(flag)
print(Meaning)


        