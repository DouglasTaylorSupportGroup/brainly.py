import requests
from bs4 import BeautifulSoup as bs
from brainly import api

with open("cookie.txt", 'rb') as f:
    cookieTxt = f.read()

url = "https://brainly.com/question/13832829"
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0"

a = api.answer(url, cookieTxt, userAgent)
print(a)