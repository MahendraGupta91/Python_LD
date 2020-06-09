
# This is update new word in dictionary at last
#load the new word at starting
import tkinter
import json
from tkinter import* 
from tkinter import Toplevel
import time
import sys
import os
import requests
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from time import strftime
WELCOME_DURATION =5000
#chrome_options = Options()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--disable-gpu')
#driver = webdriver.Chrome(options=chrome_options)
#sys.path.append(os.path.abspath("SO_site-packages"))

import pyperclip
recent_value = ""

with open('dictionary_words.json') as dict_reader:
        #print("dictionary_words Opened")
        #print(type(dict_reader))
    oldWords=json.load(dict_reader)

# It Will update new words in json file
def update_Words(newWords):
        #print(newWords)
        #print("Update_Word Called")
        #with open('dictionary_words.json') as dict_reader:
        #print("Dictionary is red..............0")
        #print(json.load(dict_reader))
        #print('......................1')
        #oldWords=json.load(dict_reader)
        #print('......................2')
        oldWords.update(newWords)
        #print(oldWords)
        
    #with open('dictionary_words.json', 'w') as dict_writer:
        #json.dump(oldWords, dict_writer)
        #print("Dictionary is written")
       # newWords={}
# It will search the word and return if found
def update_text_dictionary():
    with open('dictionary_words.json', 'w') as dict_writer:
        json.dump(oldWords, dict_writer)
        #print("Dictionary written")
        root.destroy()
    
def word_search(word):
    #print("Word Search Called")
    
        #print(oldWords)
        #print("dictionary Words")
        if word in oldWords.keys():
            #print("Search Condition is True")
            return True, oldWords[word]
        else:
            #print("Search Condition is false")
            return False, "Word Not Found"
        
def word_collector(_word,_meaning):
    #print("Word_collector Search Called")
    newWords={}
    newWords[_word]=_meaning
    #print(newWords)
    return newWords
def message_setter(meaning):
    #print("Message setter Called")
    top = Toplevel()
    ##top.title(word)
    Message(top,text=meaning, padx=20, pady=20).pack()
    top.after(WELCOME_DURATION, top.destroy)
    
    
def word_web_search(word):
    #print("Word_web_Search Called")
    #driver.get("https://dictionary.cambridge.org/dictionary/english/"+word)
    URL = "https://dictionary.cambridge.org/dictionary/english/"+word
    page= requests.get(URL)
   #content=page.page_source
    soup=BeautifulSoup(page.content,"lxml")   
    #for row in soup.find_all('div',attrs={"class" : "def ddef_d db"}):
    #print("...................................................................")
    row=soup.find_all('div',attrs={"class" : "def ddef_d db"})
    if len(row)!=0:
        string=row[0].text
        word_meaning=string.strip(' :')
        message_setter(word_meaning)
        newWord=word_collector(word,word_meaning)
        update_Words(newWord)
        #print(string)
    else:
        string="Meaning not found!"
        message_setter(string)
        #print(string)
        

#D = time.strftime("%D")
#r = time.strftime("%r")
def welcome():  
            #print("Function Started")
            recent_value=pyperclip.paste()
            #while True:
            tmp_value = pyperclip.paste()
            #if tmp_value != recent_value:
            recent_value = tmp_value
            word=recent_value.strip('')
            #print(word)
            if(len(word)<50):
                search_flag,search_result=word_search(word)
                if search_flag == True:
                    #print("Found in the dictionary")
                    message_setter(search_result)
                else:
                    #print("Word is searchnig on web")
                    word_web_search(word) 
                
#                driver.get("https://dictionary.cambridge.org/dictionary/english/"+word)
#                content=driver.page_source
#                soup=BeautifulSoup(content,"lxml")   
#                #for row in soup.find_all('div',attrs={"class" : "def ddef_d db"}):
#                #print("...................................................................")
#                row=soup.find_all('div',attrs={"class" : "def ddef_d db"})
#                if len(row)!=0:
#                    string=row[0].text
#                    WELCOME_MSG=string.strip(' :')
#                else:
#                    string="Meaning not found!"
#                    WELCOME_MSG=string.strip(' :')
#                print(string)
            else:
                string="Invalid Word"
                message_setter(string)
#                WELCOME_MSG=string.strip(' :')
                #Sprint(string)
                
#            top = Toplevel()
#            #top.title(word)
#            Message(top,text=WELCOME_MSG, padx=20, pady=20).pack()
#            top.after(WELCOME_DURATION, top.destroy)
        
                #print("Value changed: %s" % str(recent_value)[:20])
                #with open('out_clipboard.txt', '+a') as output:
                #try:
                #output.write("[Start]----------------"+D+" "+r+"----------------\n")
                #output.write("%s\n\n" % str(tmp_value))
                #output.write("[End]-----------------------------------------------------------------\n\n\n")
                #except:
                #output.write("[Start]----------------" + D + " " + r+"----------------\n")
                #output.write("%s\n\n" % str(tmp_value.encode('UTF-8')))
                #output.write("[End]-----------------------------------------------------------------\n\n\n")
                #time.sleep(0.1)
root =tkinter.Tk()
root.geometry('200x100')
tkinter.Button(root, text="Click to register", command=welcome).pack()
root.protocol("WM_DELETE_WINDOW", update_text_dictionary)
root.mainloop()
    
    
    
    
    
    
    
    
    
    
    
