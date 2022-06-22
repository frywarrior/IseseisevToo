from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://www.ilmateenistus.ee/wp-content/themes/emhi2013/data/radar/cappi_rain/?C=M;O=D"
print(url[:-8])
html = urlopen(url).read()

soup = BeautifulSoup(html, features="html.parser")

last_link = soup.find_all('a', href=True)[5]

latest_content = urlopen(f"{url[:-8]}{last_link['href']}").read()

print(last_link['href'])
