
import json
from tkinter import* 

import time
import sys
import os
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from time import strftime
WELCOME_DURATION = 5000
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=chrome_options)
sys.path.append(os.path.abspath("SO_site-packages"))
import pyperclip
recent_value = ""

## It Will update new words in json file
#def update_Words(newWords):
#    #print(newWords)
#    #print("Update_Word Called")
#    with open('dictionary_words.json') as dict_reader:
#        #print("Dictionary is red..............0")
#        #print(json.load(dict_reader))
#        #print('......................1')
#        oldWords=json.load(dict_reader)
#        #print('......................2')
#        oldWords.update(newWords)
#        #print(oldWords)
#    with open('dictionary_words.json', 'w') as dict_writer:
#        json.dump(oldWords, dict_writer)
#        #print("Dictionary is written")
#       # newWords={}
## It will search the word and return if found
##def word_search(word):
#    #print("Word Search Called")
#    with open('dictionary_words.json') as dict_reader:
#        #print("dictionary_words Opened")
#        #print(type(dict_reader))
#        oldWords=json.load(dict_reader)
#        #print(oldWords)
#        #print("dictionary Words")
#        if word in oldWords.keys():
#            #print("Search Condition is True")
#            return True, oldWords[word]
#        else:
#            #print("Search Condition is false")
#            return False, "Word Not Found"
#        
#def word_collector(_word,_meaning):
#    #print("Word_collector Search Called")
#    newWords={}
#    newWords[_word]=_meaning
#    #print(newWords)
#    return newWords
#def message_setter(meaning):
#    #print("Message setter Called")
#    top = Toplevel()
#    ##top.title(word)
#    Message(top,text=meaning, padx=20, pady=20).pack()
#    top.after(WELCOME_DURATION, top.destroy)
#    
    
#def word_web_search(word):
    #print("Word_web_Search Called")
driver.get("https://www.vocabulary.com/lists/194479")
content=driver.page_source
soup=BeautifulSoup(content,"lxml") 
dict={}  
    #for row in soup.find_all('div',attrs={"class" : "def ddef_d db"}):
    #print("...................................................................")
word=soup.find_all('a',attrs={"class" : "word dynamictext"})
meaning=soup.find_all('div',attrs={"class" : "definition"})
if len(word)==len(meaning):
    print('Both are Equal which is =')
    print(len(word))
    for x in range(len(word)):
        dict[word[x].text]=meaning[x].text
        
with open('HighFrequency_words_vocab.json', 'w') as dict_writer:
        json.dump(dict, dict_writer)
        print("Dictionary is written")   
    
    
    
    
