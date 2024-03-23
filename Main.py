"""
Web Scraper for Persian Crypto Currency Purpose
Author : Porya M. Nilaore
Date 22 March, 2024 
"""

# Import essential modules:
import requests
import urllib.request
import re # import this for extract using Regular Expression
from bs4 import BeautifulSoup as bs # import this library for using BeautifulSoup
import mechanicalsoup as ms

# Define websites data:
## TODO: I have to create a CSV file for store urls data and the insert here with loop function (module creation preferred)
Raw_data = {
    # WebSite Name : ['Url', 'Crypto_Key', 'Special_Key', 'regex_key'] 
    'BitBarg'   :   ["https://bitbarg.com/live-price", "usdtPrice", "}", "Price.*}}"],
    'PayWM'     :   ["https://paywm.net/", "p", "ml1 coinInfob", "ml2 coinInfob", "USDT=.*Rial"],
    'Nobitex'   :   ["https://api.nobitex.ir/v2/orderbook/USDTIRT", "lastTradePrice", '",', "regex_key"], #https://documenter.getpostman.com/view/5722122/Szmcayjw
}

## Adding a few more headers to get the data
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
       
# Function for extract data from websites:
def ext_func(url, crypto_key, special_key, header):
    # url is the website of exchange, crypto_key is the goal crypto for checking and special_key is the end of searching keyword
    ## Extract data from website:
    req = urllib.request.Request(url, None, header)
    response = urllib.request.urlopen(req)
    bytes_data = response.read()
    html_data = bytes_data.decode("utf-8")
    
    ## Find the index of key:
    Crypto_index = html_data.find(crypto_key)
    Total_len = Crypto_index + len(crypto_key)
    Final_len = html_data.find(str(special_key), Total_len)
    Price_tmp = html_data[Total_len:Final_len]
    
    ## Extract the price as integer:
    Price_dgt = [int(i) for i in Price_tmp if i.isdigit()]
    Price = ""
    for i in Price_dgt:
        Price = Price + str(i)
    
    Price = int(Price)
    
    return Price

def ext_func_regex(url, regex_key, header):
    ## Extract data from website:
    req = urllib.request.Request(url, None, header)
    response = urllib.request.urlopen(req)
    bytes_data = response.read()
    html_data = bytes_data.decode("utf-8")
    
    ## Extract the price as integer:
    Price_tmp = str(re.findall(regex_key, html_data))
    Price_dgt = [int(i) for i in Price_tmp if i.isdigit()]
    Price = ""
    for i in Price_dgt:
        Price = Price + str(i)
    
    Price = int(Price)
    
    return Price

def ext_func_mech(url, tag, class_buy, class_sell, regex_key):
    
    # Ineract with form:
    browser = ms.Browser()
    ##url = "https://paywm.net/"
    main_page = browser.get(url)
    ## TODO: check if response is 200
    html_page = main_page.soup

    data_buy = str(html_page.find(str(tag), class_=str(class_buy)))
    data_sell = str(html_page.find(str(tag), class_=str(class_sell)))
    
    price_buy_tmp = str(re.findall(regex_key, data_buy))
    
    price_buy_dgt = [int(i) for i in price_buy_tmp if i.isdigit()]
    price_buy = ""
    for i in price_buy_dgt:
        price_buy = price_buy + str(i)
    
    price_buy = int(price_buy)
    ## TODO: clear the texts
    
    price_sell_tmp = str(re.findall(regex_key, data_sell))
    
    price_sell_dgt = [int(i) for i in price_sell_tmp if i.isdigit()]
    price_sell = ""
    for i in price_sell_dgt:
        price_sell = price_sell + str(i)
    
    price_sell = int(price_sell)
    
    return price_buy , price_sell 

BitBarg = ext_func(Raw_data["BitBarg"][0], Raw_data["BitBarg"][1], Raw_data["BitBarg"][2], hdr)
PayWM   = ext_func_mech(Raw_data["PayWM"][0], Raw_data["PayWM"][1], Raw_data["PayWM"][2], Raw_data["PayWM"][3], Raw_data["PayWM"][4])
NobiTex = ext_func(Raw_data["Nobitex"][0], Raw_data["Nobitex"][1], Raw_data["Nobitex"][2], hdr)

print("------------------------")
print("BitBarg : " + str(BitBarg))
print("PayWM-Buy :" + str(PayWM[0]) + " PayWM-Sell : " + str(PayWM[1]))
print("NobiTex : " + str(NobiTex))
print("------------------------")


# Powered by PMNilaore in GeneralPMN Group @pmne324