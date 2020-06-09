import tkinter as tk
import json
from tkinter import Toplevel
import time
import sys
import os
import requests
#from selenium.webdriver.chrome.options import Options
#from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from functools import partial 
from time import strftime
import pyperclip
word_type={"adjective":"adj","Adjective":"adj",
           "Adjective":"adj","Adj":"adj", "Noun":"n","noun":"n",
           "n":"n","Verb":"v","verb":"v","V":"v","v":"v",
           "preposition":"pre","determiner":"det"}
newWords={"1":{"En":"One","Hi":"ek"}}
recent_value = ""
WELCOME_DURATION =20000
Eng_meaning=""
Hindi_meaning=""


root = tk.Tk()
root.iconbitmap("BlackLogo.ico")
root.title("LearnDifferences.org")
root.configure(bg='#1A5266')

with open('LD_dict_words_1May.json') as dict_reader:
        #print("dictionary_words Opened")
        #print(type(dict_reader))
    oldWords=json.load(dict_reader)


#action_with_arg=meaning_window(Eng_meaning,Hindi_meaning)
def update_Words(newWords):
        oldWords.update(newWords)
        
        
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


def Hindi_word_web_search(word): 
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
        
def update_text_dictionary():
    with open('LD_dict_words_1May.json', 'w') as dict_writer:
        json.dump(oldWords, dict_writer)
        root.destroy()
def Eng_meaning_formatting(Eng_meaning):
    str2=Eng_meaning
    str1=Eng_meaning.split(":")
    try:    
        Eng_meaning=str1[0]+"\n"+str1[1]
        return Eng_meaning
    except:
            return str2

def word_collector(_word,Eng_meaning,Hindi_meaning):
    #print("Word_collector Search Called") 
    newWords[_word]={"En":Eng_meaning,"Hi":Hindi_meaning}
    return newWords

def clipboard_word():  
            #print("Function Started")
            recent_value=pyperclip.paste()
            #while True:
            tmp_value = pyperclip.paste()
            #if tmp_value != recent_value:
            recent_value = tmp_value
            word=recent_value.strip(' ')
            #print(word)
            if(len(word)<50):
                search_flag,search_result=word_search(word)
                if search_flag == True:
                    #print("Found in the dictionary")
                    Eng_meaning=Eng_meaning_formatting(search_result["En"])
                    meaning_window(word,Eng_meaning,search_result["Hi"])
                else:
                    #print("Word is searchnig on web")
                    flag_H,Hindi_meaning=Hindi_word_web_search(word)
                    flag_E,Eng_meaning=Eng_word_web_search(word)
                    if flag_E==True:
                         Eng_meaning=Eng_meaning_formatting(Eng_meaning)
                         meaning_window(word,Eng_meaning,Hindi_meaning)
                         newWords[word]={"En":Eng_meaning,"Hi":Hindi_meaning}                         
                         update_Words(newWords)
                    else:
                        string="Not Found"
                        meaning_window(word,string,string)
            else:
                string="Invalid Word"
                meaning_window(word,string,string)
def Entry_Field_word(E_word):  
    
            word=E_word.strip(' ')
            #print(word)
            if(len(word)<50):
                search_flag,search_result=word_search(word)
                if search_flag == True:
                    #print("Found in the dictionary")
                    Eng_meaning=Eng_meaning_formatting(search_result["En"])
                    meaning_window(word,Eng_meaning,search_result["Hi"])
                else:
                    #print("Word is searchnig on web")
                    flag_H,Hindi_meaning=Hindi_word_web_search(word)
                    flag_E,Eng_meaning=Eng_word_web_search(word)
                    if flag_E==True:
                         Eng_meaning=Eng_meaning_formatting(Eng_meaning)
                         meaning_window(word,Eng_meaning,Hindi_meaning)
                         newWords[word]={"En":Eng_meaning,"Hi":Hindi_meaning}                         
                         update_Words(newWords)
                    else:
                        string="Not Found"
                        meaning_window(word,string,string)
            else:
                string="Invalid Word"
                meaning_window(string,string)

def meaning_window(word,Eng_meaning,Hindi_meaning):
    win = tk.Toplevel(root)
    win.iconbitmap("BlackLogo.ico")
    win.rowconfigure(1, weight=1)
    win.columnconfigure(1, weight=1)
    win.title("Meaning")
    win.after(WELCOME_DURATION, win.destroy)
    f1 = tk.Frame(win, height=30, bg='#1A5266')
    #f1.grid_propagate(0)
    f1.grid(row=0, column=0,sticky="nsew")
    f0=tk.Frame(win,bg="#effbfe")
    f0.grid(row=1, column=0,sticky="nsew")
    
    f2 = tk.Frame(f0,height=100,bg='#effbfe')
    f3 = tk.Frame(f0,height=100,bg='#effbfe')
    f4 = tk.Frame(f0,height=100,bg='#effbfe')
    f5 = tk.Frame(f0,height=100,bg='#effbfe')
                  
    #f2.grid_propagate(0)
    f2.grid(row=0, column=0,sticky="nsew")
    f3.grid(row=0, column=1,sticky="nsew")
    f4.grid(row=1, column=0,sticky="nsew")
    f5.grid(row=1, column=1,sticky="nsew")
    tk.Label(f1, text=word, bg='#1A5266', fg="white",font="Times 16 bold",anchor="e").grid()
    #tk.Label(f2, text="FRAME 2",fg="black",bg='#effbfe', width=20,font="Helvetica 16",anchor="e").grid()
    tk.Message(f2,text="E:",fg="black",bg='#effbfe',font="Times 14", anchor="e").grid()
    tk.Message(f3,text=Eng_meaning,fg="black",bg='#effbfe',font="Times 14").grid()
    tk.Message(f4,text="H:",fg="black",bg='#effbfe',font="Times 14", anchor="e").grid()
    tk.Message(f5,text=Hindi_meaning,fg="black",bg='#effbfe',font="Times 14").grid()

def get_word(E_word):
    Entry_Field_word(E_word.get())


E_word = tk.StringVar()    
call_get_word = partial(get_word,E_word)

hi=tk.Frame(root,height=10,width=200,bg='#1A5266').grid(column=0,row=0)
#tk.Label(hi,text="FRAME1ffffffff", bg='#1A5266', fg="white",font="Times 16 bold", LEFT).grid()
#tk.Label(hi,text="Type the word:", bg='white',fg="white").grid()

e1=tk.Entry(root, text="ABC",textvariable=E_word).grid(column=0, row=1)
tk.Frame(root,height=5,width=200,bg='#1A5266').grid(column=0,row=2)
tk.Button(root, text="submit",command=call_get_word).grid(column=0, row=3)
tk.Frame(root,height=20,width=200,bg='#1A5266').grid(column=0,row=4)
tk.Button(root, text="Clipboard",command=clipboard_word).grid(column=0, row=5)
inst=tk.Frame(root,height=2,width=200,bg='#1A5266').grid(column=0,row=6)
tk.Label(inst,text="To get meaning, type and press submit \n or copy the word and press clipboard",fg="white",bg='#1A5266').grid()

#root.after(10, meaning_window)
root.protocol("WM_DELETE_WINDOW", update_text_dictionary)
root.mainloop()