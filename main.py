#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

flight_test = FlightSearch()
flight_test.set_params(fly_to="JFK")
flight_test.call_api()

# import json

# with open("flight_data.json", "r") as f:
#     data = json.load(f)

# value_lowest_price = data["data"][0]["price"]
# print(type(data["data"]))
# index_lowest_price = 0
# for x in data["data"]:
#     print(x["price"])
#     if x["price"] < value_lowest_price:
#         index_lowest_price = x
#         value_lowest_price = x["price"]

cheapest_data = FlightData()
print(f"Cheapest flight for us 2 is: ${cheapest_data.get_lowest_price()}")
print(f"Cheapest date to leave: {cheapest_data.get_date_depart()}")
print(f"Duration of trip: {cheapest_data.get_nights()}.")
print(f"Airline: {cheapest_data.get_airline()}")
print(f"We'd fly back on the {cheapest_data.get_date_return()}.")