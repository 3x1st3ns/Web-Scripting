#!/usr/bin/env python3

from bs4 import BeautifulSoup
import urllib.request
import os
import sys

if len(sys.argv) != 2:
    print("\n[!] Uso: python3 " + sys.argv[0] + " <https://example.com>\n")
    sys.exit(1)


if __name__ == "__main__":
  try:
    print("\n")
    web = sys.argv[1]
    data = urllib.request.urlopen(sys.argv[1]).read().decode()

    soup = BeautifulSoup(data)
    tags = soup('a')
    for tag in tags:
      print(tag.get('href'))
      print("\n")
  except: 
    print("[!] Please write good the URL <https://www.example.com>\n")
