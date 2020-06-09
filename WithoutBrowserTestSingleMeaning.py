from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=chrome_options)
word="festival"
driver.get("https://dictionary.cambridge.org/dictionary/english/"+word)
content=driver.page_source
soup=BeautifulSoup(content,"lxml")
#print(soup.text)
    
#main()
row=soup.find_all('div',attrs={"class" : "def ddef_d db"})    
#for row in soup.find_all('div',attrs={"class" : "def ddef_d db"}):
print("...................................................................")
string=row[0].text
print(string.strip(' :')) 
    