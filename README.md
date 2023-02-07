# Data scraper

## Description:

## Used technology:

- ### Docker & Docker-Compose
- ### Selenium
- ### Python3.8
- ### BeautifulSoup4

## Installation:

```
docker-compose up -d
```

```
pip install requirements.txt
```

## How does it work

1. Selenium scrap all available pages and save to array links of first car at page
2. Used requests and get raw html  from every link of array
3. Obtaining necessary information using BS4
