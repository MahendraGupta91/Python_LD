from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
driver = webdriver.Chrome("chromedriver")
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.merriam-webster.com/dictionary/lethal")
#driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq")
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'important-blue-link'}):
    name=a.find('spam', attrs={'class':'dtText'})
    price=a.find('strong', attrs={'class':'mw_t_bc'})
    rating=a.find('p', attrs={'class':'hword2'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)
   # print(name)
#    _1vC4OE _2rQ-NK
    #<a class="important-blue-link" href="/dictionary/adjective">adjective</a>