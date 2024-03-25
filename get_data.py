"""
This is module is for getting data from websites. In this module I try to use more than 1 method
for this purpose.
"""
# Import require libraries:
import requests
import urllib.request
import mechanicalsoup as ms

# insert headers for solve problem in getting data from websites
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

# Class for get html data from website:
class extract_data:
       def __init__(self, url, header):
              self.url = url
              self.header = header
              
       def get_data(self):
              req = urllib.request.Request(self.url, None, self.header)
              response = urllib.request.urlopen(req)
              bytes_data = response.read()
              html_data = bytes_data.decode("utf-8")
              
              return html_data

# Class for interact with website
class extract_data_mechanical:
       def __init__(self, url, header):
              self.url = url
              self.header = header
              
       def get_data(self):
              browser = ms.Browser()
              main_page = browser.get(self.url)
              html_data = main_page.soup
              
              return html_data           
       
q = extract_data_mechanical("https://bitbarg.com/live-price",hdr)
print(q.get_data())