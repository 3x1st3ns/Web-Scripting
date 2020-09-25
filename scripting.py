# Web Scripting
from bs4 import BeautifulSoup
import urllib.request

print("******************************** WebScripting [Empezando] ***********************************")

web = input("Put the website [https://www.website.com/] :")
print("\n")
data = urllib.request.urlopen(web).read().decode()
print(data)

soup = BeautifulSoup(data)
tags = soup('a')
for tag in tags:
    print(tag.get('href'))

print("\n****************************** WebScripting [Terminado] *************************************")
