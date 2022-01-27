import requests
from bs4 import BeautifulSoup as bs

headers = {
    "Host": "brainly.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Cookie": "datadome=YJilHz-Cv01kFKRpCchUE7uc65ald7mWcazETkQKkkpBF~YdpJJdGolh~d8F5QTc14Drf9djwkwN7e7mJo.59PJYP7LT1iW3iTdnJFN_0HyCTl6zAhrc0euKdyTu0hf; Zadanepl_cookie[Token][Guest]=7DIX8coeLHhcza0fVpeAUwT8FV52GNJo5szWCDXTYQp9aW3Q8zobXT9SOfDAtUyPVmz4Om2IEv5NgSoO",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
}
p = requests.get(url="https://brainly.com/question/17561883", headers=headers)
print(p.text)
