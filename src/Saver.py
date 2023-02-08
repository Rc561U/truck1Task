import requests
from selenium.webdriver.common.by import By
import json
import os


class Saver:
    def __init__(self):
        self.create_json_file()

    def create_json_file(self):
        with open("result.json", 'w') as file:
            data = {"ads": []}
            json.dump(data, file)
        dir = os.path.join(os.getcwd(), 'data')
        if not os.path.exists(dir):
            os.mkdir(dir)

    def save_images(self, ids, images):
        dir = os.path.join(os.getcwd(), f"data/{ids}")
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

            with open(f"data/{ids}/{fname}", 'wb') as handler:
                handler.write(img_data)

    @staticmethod
    def save_data_to_json(data):
        with open("result.json", "w") as data1:
            json.dump(data, data1, indent=4, ensure_ascii=False)

    def save_vehicle_data(self, holder):
        with open("result.json", ) as file:
            data = json.load(file)
            data['ads'].append({
                'id': int(holder.get_id),
                'href': holder.get_vehicle_page,
                'title': holder.get_title,
                'price': holder.get_price,
                'color': holder.get_color,
                'power': holder.get_power,
                'mileage': holder.get_mileage,
                'description': holder.get_text,
            })
            self.save_data_to_json(data)
