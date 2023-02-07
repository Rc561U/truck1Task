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
    # options.add_argument("--headless")
    options.add_argument("- incognito")
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    # return webdriver.Remote('http://selenium:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME,
    #                         options=options)
    return webdriver.Chrome(options=options)


def get_first_vehicle(driver):

    element = driver.find_element(By.CLASS_NAME, "detail-page-link")
    print(element)


if __name__ == "__main__":
    driver = get_chrome_driver()
    driver.get("https://www.truckscout24.de/transporter/gebraucht/kuehl-iso-frischdienst/renault")
    time.sleep(3)
    # res = driver.find_element(By.CLASS_NAME, "ls-titles")
    res = driver.find_element(By.XPATH, "//div[a/@data-item-name='detail-page-link']")
    print(res)

    driver.close()

