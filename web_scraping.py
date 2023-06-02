from bs4 import BeautifulSoup as soup
from urllib.request import urlopen


def scraping_websites():
    page_url = 'http://www.zomato.com/hyderabad/biryani-crave-malakpet/order'
    client_url = urlopen(page_url)#, headers = {'User-agent': 'Mozilla\5.0'})
    page_html = client_url.read()
    client_url.close()
    page_soup = soup(page_html, 'html.parser')

    containers = page_soup.findAll('div', {'class': 'sc-fEUNkw gAkuDn'})
    print(len(containers))
    print(soup.prettify(containers[0]))


scraping_websites()
