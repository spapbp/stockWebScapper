import bs4
import alert

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.newegg.com/p/pl?d=3070+graphics&cm_sp=KeywordRelated-_-3070-_-3070+graphics-_-INFOCARD&N=601357282%20100007709"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsering
page_soup = soup(page_html, "html.parser")

#grabs each product
cells = page_soup.findAll("div", {"class":"item-cell"})

#put each cell in cell and grab title
for cell in cells:
    title = cell.findAll("a", {"class":"item-title"})
    price = cell.findAll("li", {"class": "price-current"})
    stock = cell.find("p", {"class": "item-promo"})

    #if there is a p tad with class item-promo then check if it is equal to "OUT OF STOCK" else email name and price
    if stock != None:
        if cell.div.div.p.text == "OUT OF STOCK":
            pass
        else:
            name = title[0].text
            price = price[0].strong.text + price[0].sup.text
            concat = name + '\n' + price
            #alert.email_alert("Your_Email", "IN STOCK", concat)
