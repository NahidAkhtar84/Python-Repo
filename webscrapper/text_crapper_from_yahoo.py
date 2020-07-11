# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 21:41:03 2020

@author: User
"""

from bs4 import BeautifulSoup
import requests


search = input("Search Term:")
params = {"q": search}
r = requests.get("https://search.yahoo.com/search", params=params)


soup = BeautifulSoup(r.text, "html.parser")

results = soup.find("div", {"id": "results"})

links = results.findAll("div", {"class": "algo"})

for item in links:

    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print(item_text)
        print(item_href)
        print("Summary:", item.parent.find("p", {"class": "fz-ms lh-1_43x"}).text)
