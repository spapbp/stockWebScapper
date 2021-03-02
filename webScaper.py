import bs4
import alert

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.newegg.com/p/pl?d=3070+graphics&cm_sp=KeywordRelated-_-3070-_-3070+graphics-_-INFOCARD&N=601357282%20100007709"
#my_url = "https://www.amazon.com/AMD-Ryzen-5800X-16-Thread-Processor/dp/B0815XFSGK"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsering
page_soup = soup(page_html, "html.parser")

#grabs each product
cells = page_soup.findAll("div", {"class":"item-cell"})

#put each cell in cell and grab title

'''
for cell in cells:
    title = cell.findAll("a", {"class":"item-title"})
    print(title[0].text)

    if cell.div.div.p.text == "OUT OF STOCK":
        #print(cell.div.div.p.text)
        price = cell.findAll("li", {"class": "price-current"})
        name = title[0].text
        
        
    
    else:
        price = cell.findAll("li", {"class": "price-current"})
        print(price[0].strong.text, price[0].sup.text)
'''



for cell in cells:
    title = cell.findAll("a", {"class":"item-title"})
    price = cell.findAll("li", {"class": "price-current"})
    stock = cell.find("p", {"class": "item-promo"})

    if stock != None:
        if cell.div.div.p.text == "OUT OF STOCK":
            pass
            '''
            name = title[0].text
            print(name)

            nums = price[0].strong.text + price[0].sup.text
            print(name)
            concat = name + '\n' + nums
            print(nums)
            #alert.email_alert("4042422725@txt.att.net", "IN STOCK", concat)
            '''
        else:
            name = title[0].text
            print(name)

            nums = price[0].strong.text + price[0].sup.text
            print(name)
            concat = name + '\n' + nums
            print(nums)
            #alert.email_alert("4042422725@txt.att.net", "IN STOCK", concat)