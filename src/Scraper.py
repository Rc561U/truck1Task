from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from Saver import Saver
from Holder import Holder


class Scraper:

    def __init__(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("- incognito")
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument("--no-sandbox")
        options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(options=options)
        self.saver = Saver()
        self.holder = Holder()

    def get_next_page(self):
        self.driver.get(self.holder.get_current_page)
        next_page = self.driver.find_element(By.XPATH, "//li[@class='next-page']//a[contains(@href,'')]")
        self.holder.get_current_page = next_page.get_attribute('href')
        self.holder.get_next_page = True if self.holder.get_current_page else False

    def detail_vehicle_link(self):
        self.driver.get(self.holder.get_current_page)
        res = self.driver.find_elements(By.XPATH, "//a[@data-item-name='detail-page-link']")
        self.holder.get_vehicle_page = res[0].get_attribute('href')

    def get_vehicle_data(self):
        self.driver.get(self.holder.get_vehicle_page)
        self.holder.get_price = self.driver.find_element(By.CLASS_NAME, "d-price").text
        self.holder.get_title = self.driver.find_element(By.CLASS_NAME, "sc-ellipsis").text
        self.holder.get_text =  self.driver.find_element(By.XPATH, "//div[@data-type='description']").text
        description = self.driver.find_element(By.XPATH, "//ul[@class='columns']").find_elements(By.TAG_NAME, "li")
        for equal in description:
            first_elem, second_elem = equal.text.split('\n')
            if first_elem == "Farbe": self.holder.get_color = second_elem
            if first_elem == "Leistung": self.holder.get_power = second_elem
        self.holder.get_mileage = self.driver.find_elements(By.XPATH, "//div[@class='itemspace']")
        self.holder.get_id = self.holder.get_vehicle_page.split('/')[-2]
        self.save_images()

    def save_images(self):
        images = self.driver.find_elements(By.XPATH, "//div[@class='gallery-picture']")
        self.saver.save_images(self.holder.get_id, images)

    def main(self):
        while self.holder.get_next_page:
            print('Start scraping the page ==>')
            self.detail_vehicle_link()
            self.get_vehicle_data()
            self.saver.save_vehicle_data(self.holder)
            self.get_next_page()
            print('Finish the page scraping <==\n')


if __name__ == "__main__":
    new = Scraper()
    new.main()
