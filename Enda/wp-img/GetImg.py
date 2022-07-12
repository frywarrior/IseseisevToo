def getimg():
    from bs4 import BeautifulSoup
    from urllib.request import urlopen, urlretrieve

    url = "https://vana.ilmateenistus.ee/wp-content/themes/emhi2013/data/radar/cappi_rain/?C=M;O=D"

    html = urlopen(url).read()

    soup = BeautifulSoup(html, features="html.parser")

    last_link = soup.find_all('a', href=True)[5]

    urlretrieve(f"{url[:-8]}{last_link['href']}", "static/img.png")

    print(last_link['href'])

    print(f"{url[:-8]}{last_link['href']}")
