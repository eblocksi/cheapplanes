import datetime
import os
import requests
import json
from dotenv import load_dotenv

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        load_dotenv('data.env')
        self.headers = {
            "apikey": os.getenv('TEQ_KEY')
        }
        self.endpoint = os.getenv('TEQ_ENDPOINT')
        self.params = {}
        self.today = self.set_date_format(datetime.datetime.today() + datetime.timedelta(days=175)) 
        self.one_year = self.set_date_format(datetime.datetime.today() + datetime.timedelta(days=210))
        self.set_params()

    def set_date_format(self, unformatted_date, frmt=f"%d/%m/%Y"):
        '''
        Returns the datetime as a "dd/mm/yyyy" string
        '''
        return unformatted_date.strftime(frmt)
    def set_params(self, fly_from="CDG", fly_to="ICN", 
                   date_from=None, date_to=None, 
                   nights_in_dst_from="7", nights_in_dst_to="28", 
                   flight_type="round", adults="2"):
        if date_from is None:
            date_from = self.today

        if date_to is None:
            date_to = self.one_year

        self.params = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": nights_in_dst_from,
            "nights_in_dst_to": nights_in_dst_to,
            "flight_type": flight_type,
            "max_stopovers": "0",
            "one_per_date": "1",
            "adults": adults,
            "limit": "10",
        }

    def call_api(self):
        # print(f"{self.endpoint}?/{self.headers}")
        response = requests.get(url=self.endpoint, params=self.params, headers=self.headers)
        data = json.loads(response.text)
        # print(response.status_code)
        data = data['data'][:5]
        with open("flight_data.json", "w") as f:
            json.dump(data, f)