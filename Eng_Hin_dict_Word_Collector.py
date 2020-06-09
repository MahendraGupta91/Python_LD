
import requests
import json
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re
from time import strftime
word_type={"adjective":"adj","Adjective":"adj",
           "Adjective":"adj","Adj":"adj", "Noun":"n","noun":"n",
           "n":"n","Verb":"v","verb":"v","V":"v","v":"v",
           "preposition":"pre","determiner":"det"}
newWords={"1":{"En":"One","Hi":"ek"}}
#print("Hello_1")

def update_Words(newWords):
        #print("Word update function called")
        with open('Hindi_English_words_12Apr.json') as dict_reader:
            #print("file opened")
            oldWords=json.load(dict_reader)
            #print("Word Loaded")
            #print("File opened")
#            print(newWords)
            oldWords.update(newWords)
            print("Dict Updated  values after update ")
#            print(oldWords)
                   
        with open('Hindi_English_words_12Apr.json', 'w') as dict_writer:
            json.dump(oldWords,dict_writer)
            print("Dictionary written")
        #print('......................1')
        #oldWords=json.load(dict_reader)
        #print('......................2')
        #oldWords.update(newWords)
        #print(oldWords)
#def update_text_dictionary():
#    with open('Hindi_English_words_12Apr.json', 'w') as dict_writer:
#        json.dump(oldWords, dict_writer)
#        #print("Dictionary written")
#        root.destroy()

def Eng_word_web_search(word):
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

f = open("english13.text", "r")
#for i in range(20):
word_text=f.read()
word_text=re.split("\n",word_text)
#print(len(word_text))
for i in range(66000,66010):
    word=word_text[i].strip(' ')
    #print(word)
    flag_H,Hindi_meaning=hindi_word_web_search(word)
    flag_E,Eng_meaning=Eng_word_web_search(word)
    print(i)
#    print(flag_E)
#    print(flag_H)
    if flag_E==True:
        newWords[word]={"En":Eng_meaning ,"Hi":Hindi_meaning}
        ##print(newWords)
    if i%10==0:
        update_Words(newWords)
        print(flag_E)
        print(flag_H)
        #print("After Updation New Words")
        #print(newWords)
    #print(Hindi_meaning)
    #print(Eng_meaning)

    
        