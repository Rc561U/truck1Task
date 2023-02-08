import urllib

from selenium.webdriver.common.by import By
import json
import re
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
import datetime
import os
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


class Scraper:
    current_page = "https://www.truckscout24.de/transporter/gebraucht/kuehl-iso-frischdienst/renault?currentpage"
    vehicle_page = ''
    price = 0
    title = ''
    text = ''
    color = ''
    power = 0
    id = 0
    mileage = 0
    next_page = True

    def __init__(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("- incognito")
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument("--no-sandbox")
        options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(options=options)
        self.create_json_file()

    def create_json_file(self):
        with open("result.json", 'w') as file:
            data = {"ads": []}
            json.dump(data, file)

    def get_next_page(self):
        self.driver.get(self.current_page)
        next_page = self.driver.find_element(By.XPATH, "//li[@class='next-page']//a[contains(@href,'')]")
        self.current_page = next_page.get_attribute('href')
        self.next_page = True if self.current_page else False

    def detail_vehicle_link(self):
        self.driver.get(self.current_page)
        res = self.driver.find_elements(By.XPATH, "//a[@data-item-name='detail-page-link']")
        self.vehicle_page = (res[0].get_attribute('href'))

    def get_vehicle_data(self):
        self.driver.get(self.vehicle_page)
        self.price = self.driver.find_element(By.CLASS_NAME, "d-price").text
        self.title = self.driver.find_element(By.CLASS_NAME, "sc-ellipsis").text
        self.text = self.driver.find_element(By.XPATH, "//div[@data-type='description']").text
        description = self.driver.find_element(By.XPATH, "//ul[@class='columns']").find_elements(By.TAG_NAME, "li")
        for equal in description:
            first_elem, second_elem = equal.text.split('\n')
            if first_elem == "Farbe": self.color = second_elem
            if first_elem == "Leistung": self.power = second_elem
        self.mileage = self.driver.find_elements(By.XPATH, "//div[@class='itemspace']")[0].text
        self.id = self.vehicle_page.split('/')[-2]
        self.save_images()

    def save_images(self):
        dir = os.path.join(os.getcwd(), 'data')
        if not os.path.exists(dir):
            os.mkdir(dir)

        dir = os.path.join(os.getcwd(), f"data/{self.id}")
        if not os.path.exists(dir):
            os.mkdir(dir)
        # Images
        images = self.driver.find_element(By.XPATH, "//div[@class='as24-carousel__container']").find_elements(By.TAG_NAME, "img")
        counter = 0
        for image in images:
            if counter > 2: break
            image_link = image.get_attribute('data-src')
            print(image_link)
            urllib.urlretrieve(image_link, f"data/{self.id}")
            counter += 1
        # solve save image problem

    @staticmethod
    def save_data_to_json(data):
        with open("result.json", "w") as data1:
            json.dump(data, data1, indent=4, ensure_ascii=False)

    def save_vehicle_data(self):
        self.detail_vehicle_link()
        self.get_vehicle_data()
        with open("result.json", ) as file:
            data = json.load(file)
            data['ads'].append( {
                'id': self.id,
                'href': self.vehicle_page,
                'title': self.title,
                'price': self.price,
                'color': self.color,
                'power': self.power,
                'mileage': self.mileage,
                'description': self.text,
            })
            self.save_data_to_json(data)

    def base(self):
        self.detail_vehicle_link()
        self.get_vehicle_data()
        self.save_vehicle_data()

    def main(self):
        while self.next_page:
            self.detail_vehicle_link()
            self.get_vehicle_data()
            self.save_vehicle_data()
            self.get_next_page()


if __name__ == "__main__":
    new = Scraper()
    new.main()
