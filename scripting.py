# Web Scripting
from bs4 import BeautifulSoup
import urllib.request

print("*******************************************************************")
web = input("Put the page [https://website.com/] :")
data = urllib.request.urlopen(web).read().decode()
print(data)

soup = BeautifulSoup(data)
tags = soup('a')
for tag in tags:
    print(tag.get('href'))

print("*******************************************************************")
