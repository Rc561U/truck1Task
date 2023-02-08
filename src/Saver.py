import requests
from selenium.webdriver.common.by import By
import json
import os

from src.Holder import Holder


class Saver(Holder):
    def __init__(self):
        self.create_json_file()

    def create_json_file(self):
        with open("result.json", 'w') as file:
            data = {"ads": []}
            json.dump(data, file)
        dir = os.path.join(os.getcwd(), 'data')
        if not os.path.exists(dir):
            os.mkdir(dir)

    def save_images(self, id, images):
        dir = os.path.join(os.getcwd(), f"data/{id}")
        if not os.path.exists(dir):
            os.mkdir(dir)
        counter = 0
        for image in images:
            if counter > 2: break
            image_link = image.find_element(By.TAG_NAME, "img")
            imager = image_link.get_attribute('data-src')
            print(imager + f' Image {counter + 1} successfully downloaded')
            img_data = requests.get(imager).content
            fname = imager.split('/')[-1]
            counter += 1

            with open(f"data/{id}/{fname}", 'wb') as handler:
                handler.write(img_data)

    @staticmethod
    def save_data_to_json(data):
        with open("result.json", "w") as data1:
            json.dump(data, data1, indent=4, ensure_ascii=False)

    def save_vehicle_data(self):
        # self.get_vehicle_data()
        with open("result.json", ) as file:
            data = json.load(file)
            print(self.get_vehicl())
            data['ads'].append({
                'id': int(self.id),
                'href': self.vehicle_page,
                'title': self.title,
                'price': self.price,
                'color': self.color,
                'power': self.power,
                'mileage': self.mileage,
                'description': self.text,
            })
            self.save_data_to_json(data)
