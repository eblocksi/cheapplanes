import json


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self) -> None:
        self.ind_flight = 0
        self.flight_data = self.load_data()
        self.lowest_price = self.flight_data[0]["price"]

    def load_data(self):
        with open("flight_data.json") as f:
            data = json.load(f)
        return data
    
    def get_lowest_price(self):
        return self.flight_data[self.ind_flight]["price"]

    def get_date_depart(self):
        return self.flight_data[self.ind_flight]["route"][0]["utc_departure"].split('T')[0]

    def get_date_return(self):
        return self.flight_data[self.ind_flight]["route"][1]["utc_departure"].split('T')[0]

    def get_airline(self):
        return self.flight_data[self.ind_flight]["airlines"]

    def get_nights(self):
        return self.flight_data[self.ind_flight]["nightsInDest"]