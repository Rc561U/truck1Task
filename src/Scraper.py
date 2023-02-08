from selenium.webdriver.common.by import By
import json
import re
import os
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from Saver import Saver
from Holder import Holder

class Scraper(Holder):

    def __init__(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("- incognito")
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument("--no-sandbox")
        options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(options=options)
        self.saver = Saver()

    def get_next_page(self):
        self.driver.get(self.current_page)
        next_page = self.driver.find_element(By.XPATH, "//li[@class='next-page']//a[contains(@href,'')]")
        self.current_page = next_page.get_attribute('href')
        self.next_page = True if self.current_page else False

    def detail_vehicle_link(self):
        self.driver.get(self.current_page)
        res = self.driver.find_elements(By.XPATH, "//a[@data-item-name='detail-page-link']")
        self.vehicle_page = (res[0].get_attribute('href'))

    def formate_raw_text(self, text):
        return re.sub(r"[\n\t**]*", "", text)

    def format_raw_price(self, price):
        return "".join(re.findall(r"[\d]+", price))

    def format_raw_power(self, power):
        return "".join(re.findall(r"^[\d]+", power))

    def format_raw_mileage(self, mileage):
        for _ in mileage:
            word, value = _.text.split('\n')
            if word == "Kilometer":
                return self.format_raw_price(value)

    def get_vehicle_data(self):
        self.driver.get(self.vehicle_page)
        self.price = self.format_raw_price(self.driver.find_element(By.CLASS_NAME, "d-price").text)
        self.title = self.driver.find_element(By.CLASS_NAME, "sc-ellipsis").text
        self.text = self.formate_raw_text(self.driver.find_element(By.XPATH, "//div[@data-type='description']").text)
        description = self.driver.find_element(By.XPATH, "//ul[@class='columns']").find_elements(By.TAG_NAME, "li")
        for equal in description:
            first_elem, second_elem = equal.text.split('\n')
            if first_elem == "Farbe": self.color = second_elem
            if first_elem == "Leistung": self.power = self.format_raw_power(second_elem)
        self.mileage = self.format_raw_mileage(self.driver.find_elements(By.XPATH, "//div[@class='itemspace']"))
        self.id = self.vehicle_page.split('/')[-2]
        self.save_images()

    def save_images(self):

        images = self.driver.find_elements(By.XPATH, "//div[@class='gallery-picture']")
        self.saver.save_images(self.id, images)



    # @staticmethod
    # def save_data_to_json(data):
    #     with open("result.json", "w") as data1:
    #         json.dump(data, data1, indent=4, ensure_ascii=False)
    #
    # def save_vehicle_data(self):
    #     self.detail_vehicle_link()
    #     # self.get_vehicle_data()
    #     with open("result.json", ) as file:
    #         data = json.load(file)
    #         data['ads'].append({
    #             'id': int(self.id),
    #             'href': self.vehicle_page,
    #             'title': self.title,
    #             'price': self.price,
    #             'color': self.color,
    #             'power': self.power,
    #             'mileage': self.mileage,
    #             'description': self.text,
    #         })
    #         self.save_data_to_json(data)

    def main(self):
        while self.next_page:
            print('Start scraping the page ==>')
            self.detail_vehicle_link()
            self.get_vehicle_data()
            self.saver.save_vehicle_data()
            self.get_next_page()
            print('Finish the page scraping <==\n')


if __name__ == "__main__":
    new = Scraper()
    new.main()
