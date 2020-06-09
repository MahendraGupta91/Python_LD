from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
driver = webdriver.Chrome("chromedriver")
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.merriam-webster.com/dictionary/lethal")
#driver.get("https://www.learndifferences.org")
#driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq")
content = driver.page_source

#htmltxt = "<p>Hello World</p>"
soup = BeautifulSoup(content)
#for row in soup.find_all('div',attrs={"class" : "vg"}):
   # print (row.text)
    
for row in soup.find_all('span',attrs={"class" : "dtText"}):
    print (row.text)
#print(soup.prettify())
#abasasas=soup.text
#aaa=soup.find_all('a')
#l=len(aaa)
#print(aaa[0].get_text())
#print(aaa[1].get_text())
#print(aaa[2].get_text())