from bs4 import BeautifulSoup

with open('page_source.html') as file:
    soup = BeautifulSoup(file, "html.parser")
    items = soup.select('a[data-item-name="detail-page-link"]')
    print(items[0]['href'])
