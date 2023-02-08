import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import json
import re
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
import datetime

from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def get_chrome_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("- incognito")
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    # return webdriver.Remote('http://selenium:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME,
    #                         options=options)
    return webdriver.Chrome(options=options)


def get_first_vehicle_link(driver):
    vehicle_card_link = driver.find_element(By.XPATH, "//a[@data-item-name='detail-page-link']").get_attribute('href')


# def get_vehicle_data(vehicle_link):
#     vecicle_page = driver.get(
#         "https://www.truckscout24.de/fahrzeugdetails/Transporter-Renault-MASTER-165-35-20-C-CARR-K%C3%BChl-Iso-Frischdienst/20501838/1")
#     res = driver.find_element(By.CLASS_NAME, "d-price").text
#     print(res)


def save_data_to_json(data):
    with open("union.json", "w") as data1:
        json.dump(data, data1, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    driver = get_chrome_driver()
    driver.get("https://www.truckscout24.de/transporter/gebraucht/kuehl-iso-frischdienst/renault")
    # res = driver.find_element(By.CLASS_NAME, "ls-titles")
    res = driver.find_elements(By.XPATH, "//a[@data-item-name='detail-page-link']")
    print(res[0].get_attribute('href'))
    # print(res.get_attribute('href'))
    # nexTageLink = driver.find_element(By.XPATH, "//li[@class='next-page']//a[contains(@href,'')]")
    # driver.get(
    #     "https://www.truckscout24.de/fahrzeugdetails/Transporter-Renault-Master-165-35-K%C3%BChl-Iso-Frischdienst/20339570/1")

    ## Price
    # price = driver.find_element(By.CLASS_NAME, "d-price").text

    ## Title of vehicle
    # title = driver.find_element(By.CLASS_NAME, "sc-ellipsis").text

    ## Full Description
    # text = driver.find_element(By.XPATH, "//div[@data-type='description']").text

    # Color Power
    # description = driver.find_element(By.XPATH, "//ul[@class='columns']").find_elements(By.TAG_NAME, "li")
    # color = ''
    # power = ''
    # for equal in description:
    #     first_elem, second_elem = equal.text.split('\n')
    #     if first_elem == "Farbe": color = second_elem
    #     if first_elem == "Leistung": power = second_elem

    ## Images
    # images = driver.find_element(By.XPATH, "//div[@class='as24-carousel__container']").find_elements(By.TAG_NAME, "img")
    # counter = 0
    # for image in images:
    #     if counter > 2: break
    #     image_link = image.get_attribute('data-src')
    #     print(image_link)
    #     counter += 1
    # # solve save image problem


    # print(price)
    # print(color)
    # print(power)
    # print(title)
    # print(text)

    driver.close()
