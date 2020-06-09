from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
#driver = webdriver.Chrome("chromedriver")
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
#driver.get("https://www.merriam-webster.com/dictionary/epidemic")
#driver.get("https://www.learndifferences.org")
#driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq")
#content = driver.page_source

#htmltxt = "<p>Hello World</p>"
#soup = BeautifulSoup(content,"lxml")
#for row in soup.find_all('div',attrs={"class" : "vg"}):
   # print (row.text)
#kk=soup.find_all('span',attrs={"class" : "dtText"})
#for row in soup.find_all('span',attrs={"class" : "dtText"}):
print("...................................................................")
s=BeautifulSoup(' <span class="dtText"><strong class="mw_t_bc">: </strong>an outbreak or product of sudden rapid spread, growth, or development<span class="ex-sent first-child t no-aq sents"> an <span class="mw_t_wi">epidemic</span> of bankruptcies</span></span>',"lxml")
s1=s.text
s2=s.find('span',attrs={"class" : "ex-sent first-child t no-aq sents"})
s3=s2.text
#s2=s.findChildren('span',attrs={"class" : "dtText"})
print(s2.text)
#print(s2)