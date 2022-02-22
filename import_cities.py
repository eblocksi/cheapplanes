import json

class City_List:
    def __init__(self) -> None:
        self.cities_dict = self.get_cities()
        self.cities_list = self.convert_cities()

    def get_cities(self):
        with open('flight_data/airport_list.json', 'r') as f:
            data = json.load(f)
        return data

    def convert_cities(self):
        return [key for key in self.cities_dict.keys()]