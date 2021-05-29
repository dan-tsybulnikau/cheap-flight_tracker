from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

# Fly from
HOMETOWN = 'London'
my_data = DataManager()
# Checking IATA code for 'Fly from' city
city_from = my_data.get_hometown_code(HOMETOWN)
# Collecting IATA codes for destinations
locations_to = my_data.get_data()
# Searching for flight details
found_routes = FlightSearch(city_from, locations_to).get_flight_data()
# Checking if found price is less than desired, and sending SMS if it is
for i in range(len(found_routes)):
    if found_routes[i]['price'] <= locations_to[i]['lowestPrice']:
        message = FlightData(found_routes[i]).show_flight_data()
        notification = NotificationManager(message).send_message()
