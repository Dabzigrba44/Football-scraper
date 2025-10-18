import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/sport/football"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
headlines = soup.find_all("h3")

print("Football Headlines:")
for h in headlines[:10]:
    print("-", h.text.strip())
