
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
    def vehicle_page(self):
        return self.vehicle_page

    @vehicle_page.setter
    def vehicle_page(self, value):
        vehicle_page = value