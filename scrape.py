import requests
from bs4 import BeautifulSoup

image_page = "https://www.google.com/search?safe=strict&hl=en&tbm=isch&sxsrf=%3A1582396392044&source=hp&biw=1536&bih=754&ei=6HNRXpwM67GCB_HXvogN&q=pizza"
response = requests.get(image_page)


soup = BeautifulSoup(response.text,"html.parser")

soup.findAll("img")

one_a_tag = soup.findAll("img")[36]

print(one_a_tag)