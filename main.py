#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from import_cities import City_List
import json

def change_depart_city():
    return input("Please enter the new airport code for your departure city: ")

def change_destin_city():
    return input("Please input the new airport code for your destination city: ")


flight_test = FlightSearch()



# cheapest_data = FlightData()
# print(f"Cheapest flight for us 2 is: ${cheapest_data.get_lowest_price()}")
# print(f"Cheapest date to leave: {cheapest_data.get_date_depart()}")
# print(f"Duration of trip: {cheapest_data.get_nights()}.")
# print(f"Airline: {cheapest_data.get_airline()}")
# print(f"We'd fly back on the {cheapest_data.get_date_return()}.")


city_list = City_List()
cheap_dict = {}

for x in city_list.cities_list:

    flight_test.set_params(fly_to=x)
    flight_test.call_api()
    cheapest_data = FlightData()
    cheap_dict[x] = {
        'city': city_list.cities_dict[x],
        'airport': x,
        'price': '${:,}'.format(cheapest_data.get_lowest_price()),
        'date_from': cheapest_data.get_date_depart(),
        'nights_in_dst': cheapest_data.get_nights(),
        'airline': cheapest_data.get_airline(),
        'date_return': cheapest_data.get_date_return(),
    }
    with open("cheapest_flights.json", "w") as f:
        json.dump(cheap_dict, f)
    print(cheap_dict)

for key in cheap_dict.keys():
    for (key1,value) in cheap_dict[key].items():
        print(f"{key1} : {value}")
    print('\n')

