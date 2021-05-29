import requests
import os
import datetime


class FlightSearch:
    def __init__(self, hometown_iata: str, destination: list):
        self.hometown_iata = hometown_iata
        self.destination = destination
        self.nights_to_stay_min_max = (7, 10)
        self.from_date = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        self.to_date = (datetime.datetime.today() + datetime.timedelta(days=180)).strftime('%d/%m/%Y')
        self.result = []

    def get_flight_data(self):
        """ Using Tequila-API searches for the lowest price between tomorrow and 6 month forward for number of nights
         to stay from 7 to 14 according to hometown and destinations in Google sheet.
        Returns list for each destination """
        for city in self.destination:
            header = {'apikey': os.environ["TEQUILA_API_KEY"]}
            query = {
                'fly_from': self.hometown_iata,
                'fly_to': city['iataCode'],
                'date_from': self.from_date,
                'date_to': self.to_date,
                'sort': 'price',
                'limit': 1,
                'curr': 'EUR',
                'nights_in_dst_from': self.nights_to_stay_min_max[0],
                'nights_in_dst_to': self.nights_to_stay_min_max[1],
            }
            flight_data_response = requests.get(
                url="https://tequila-api.kiwi.com/v2/search",
                params=query,
                headers=header,
                )
            flight_data = flight_data_response.json()
            flight_info = {
                'city-from': flight_data['data'][0]['cityFrom'],
                'airport-from': flight_data['data'][0]['flyFrom'],
                'city-to': flight_data['data'][0]['cityTo'],
                'airport-to': flight_data['data'][0]['flyTo'],
                'price': flight_data['data'][0]['price'],
                'date-from': flight_data['data'][0]['route'][0]['local_departure'][0:10],
                'date-to': flight_data['data'][0]['route'][1]['local_departure'][0:10],

            }
            self.result.append(flight_info)
        return self.result
