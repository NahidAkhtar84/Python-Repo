from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os

search = input("Search for:\n")
params = {"q": search}
dir_name = search.replace(" ", "_").lower()

if not os.path.isdir(dir_name):
    os.makedirs(dir_name)

r = requests.get("https://bing.com/images/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")
links = soup.findAll("a", {"class": "thumb"})
i=0
imgType = ["JPG", "JPE", "BMP", "GIF", "PNG", "JPEG"]
for item in links:
    try:
        img_obj = requests.get(item.attrs["href"])
        print("Getting: ", item.attrs["href"])
        title = item.attrs["href"].split("/")[-1]
        try:
            img = Image.open(BytesIO(img_obj.content))
            if img.format in imgType:
                img.save("./"+ dir_name +"/" + title, img.format)
                i += 1
            else:
                continue
        except:
            print("Couldnot save the image!")
        if i == 21:
            break
    except:
        print("Could not get the image,,,")