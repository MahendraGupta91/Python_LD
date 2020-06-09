
import requests
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from time import strftime
word_type={"adjective":"adj","Adjective":"adj",
           "Adjective":"adj","Adj":"adj", "Noun":"n","noun":"n",
           "n":"n","Verb":"v","verb":"v","V":"v","v":"v",
           "preposition":"pre","determiner":"det"}

def word_web_search(word):
    try :
        URL = "https://dictionary.cambridge.org/dictionary/english/"+word
        page= requests.get(URL)
        #content=page.page_source
        soup=BeautifulSoup(page.content,"lxml")   
        #for row in soup.find_all('div',attrs={"class" : "def ddef_d db"}):
        #print("...................................................................")
        row=soup.find_all('div',attrs={"class" : "def ddef_d db"})
        
        if len(row)!=0:
            row_adj_n=soup.find_all('span',attrs={"class" : "pos dpos"})
            string1="("+word_type[row_adj_n[0].text]+"):"
            string2=row[0].text
            Eng_meaning=string1+string2.strip(' :')
#            string=row[0].text
#            Eng_meaning=string.strip(' :')     
            #print(string)
            flag_E=True
        else:
            Eng_meaning="Meaning not found!"
            flag_E=False
    except :
            Eng_meaning="Meaning not found!"
            flag_E=False
    return flag_E, Eng_meaning

flag_E,Eng_meaning=word_web_search("abbey")
print(flag_E)
print(Eng_meaning)
    
        