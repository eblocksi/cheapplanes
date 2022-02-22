import json

airports = {
    'Bangkok': 'BKK',
    'Hong Kong': 'HKG',
    'Seoul': 'ICN',
    'Tokyo': 'HND',
    'Rome': 'FCO',
    'Athens': 'ATH', 
    'New York City': 'JFK',
    'Los Angeles': 'LAX',
    'Istanbul': 'IST',
    'Kuala Lumpur': 'KUL',
    'Vienna': 'VIE',
    'Prague': 'PRG',
    'Berlin': 'SXF',
}


with open('flight_data/airport_list.json', 'w') as f:
    json.load(airports, f)