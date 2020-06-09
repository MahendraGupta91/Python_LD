import tkinter
from tkinter import* 
from tkinter import Toplevel
import time
import sys
import os
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from time import strftime
WELCOME_DURATION = 2000
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=chrome_options)
sys.path.append(os.path.abspath("SO_site-packages"))

import pyperclip
recent_value = ""


#D = time.strftime("%D")
#r = time.strftime("%r")
def welcome():
    print("Function Started")
    recent_value=pyperclip.paste()
    while True:
        tmp_value = pyperclip.paste()
        if tmp_value != recent_value:
            recent_value = tmp_value
        
            word=recent_value.strip('')
            print(word)
            driver.get("https://dictionary.cambridge.org/dictionary/english/"+word)
            content=driver.page_source
            soup=BeautifulSoup(content,"lxml")   
            #for row in soup.find_all('div',attrs={"class" : "def ddef_d db"}):
                #print("...................................................................")
            row=soup.find_all('div',attrs={"class" : "def ddef_d db"})
            string=row[0].text
            WELCOME_MSG=string.strip(' :')
            print(string)
            top = Toplevel()
            top.title(word)
            Message(top,text=WELCOME_MSG, padx=20, pady=20).pack()
            top.after(WELCOME_DURATION, top.destroy)
        
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
        time.sleep(0.1)
root =tkinter.Tk()
tkinter.Button(root, text="Click to register", command=welcome).pack()
root.mainloop()
    
    
    
    
    
    
    
    
    
    
    
