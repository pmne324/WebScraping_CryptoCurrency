"""
Web Scraper for Persian Crypto Currency Purpose
Author : Porya M. Nilaore
Date 22 March, 2024 
"""

# Import essential modules:
import urllib
from urllib.request import urlopen

# Define some variables:
url = list()
page = list()
html = list()

BitBarg = "https://bitbarg.com/live-price"
Paywm   = "https://paywm.net/"
Nobitex = "https://nobitex.ir/usdt/"

# Insert exchange websites data for scraping:
# TODO: I have to create a CSV file for store urls data and the insert here with loop function (module creation preferred)
url.append(BitBarg)
#url.append(Paywm)
#url.append(Nobitex)

# Scraping data from websites:
for i in range(len(url)):
    # TODO: open a thread and decode html_bytes right after getting url
    page.append(urlopen(url[i]))
    html_bytes = page[i].read()
    html.append(html_bytes.decode("utf-8"))
    print(str(i) + " Finished")
    
Crypto_Name = "USDT"
title_index = html[0].find("USDT")
print(html[0].find("USDT"))

# Powered by PMNilaore in GeneralPMN Group @pmne324