import re


class Holder:
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

    @property
    def get_current_page(self):
        return self.current_page

    @get_current_page.setter
    def get_current_page(self, value):
        self.current_page = value

    @property
    def get_next_page(self):
        return self.next_page

    @get_next_page.setter
    def get_next_page(self, value):
        self.next_page = value

    @property
    def get_vehicle_page(self):
        return self.vehicle_page

    @get_vehicle_page.setter
    def get_vehicle_page(self, value):
        self.vehicle_page = value

    @property
    def get_price(self):
        return self.price

    @get_price.setter
    def get_price(self, value):
        self.price = "".join(re.findall(r"[\d]+", value))

    @property
    def get_id(self):
        return self.id

    @get_id.setter
    def get_id(self, value):
        self.id = value

    @property
    def get_power(self):
        return self.power

    @get_power.setter
    def get_power(self, value):
        self.power = "".join(re.findall(r"^[\d]+", value))

    @property
    def get_color(self):
        return self.color

    @get_color.setter
    def get_color(self, value):
        self.color = value

    @property
    def get_text(self):
        return self.text

    @get_text.setter
    def get_text(self, value):
        self.text = re.sub(r"[\n\t**]*", "", value)

    @property
    def get_mileage(self):
        return self.mileage

    @get_mileage.setter
    def get_mileage(self, values):
        for _ in values:
            word, value = _.text.split('\n')
            if word == "Kilometer":
                self.mileage = "".join(re.findall(r"[\d]+", value))

    @property
    def get_title(self):
        return self.title

    @get_title.setter
    def get_title(self, value):
        self.title = value
