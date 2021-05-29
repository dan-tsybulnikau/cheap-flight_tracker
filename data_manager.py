import requests
import os


class DataManager:
    def __init__(self):
        self.endpoint = os.environ["SHEETY_GET_ENDPOINT"]
        self.header = {"Authorization": os.environ['BEARER_TOKEN']}
        self.load = requests.get(url=self.endpoint, headers=self.header)
        self.data = self.load.json()
        self.route = []
        self.row_count = 2

    def get_hometown_code(self, hometown: str):
        """Returns 'IATA Code for city's string input"""
        self.hometown = hometown.title()
        header = {'apikey': os.environ["TEQUILA_API_KEY"]}
        query = {
            'term': self.hometown,
            'location_types': 'airport',
            'limit': 1,
            'active_only': True
        }
        iata_response = requests.get(
            url="https://tequila-api.kiwi.com/locations/query",
            params=query,
            headers=header,
        )
        data = iata_response.json()
        hometown_code = data['locations'][0]['city']['code']
        return hometown_code

    def get_data(self):
        """Checks Google sheet, searches for IATA Codes for each city, and writing them to table. Returns list of
        dictionaries with 'Lowest Price' and 'IATA Code' for each city"""
        for row in self.data['prices']:
            header = {'apikey': os.environ["TEQUILA_API_KEY"]}
            query = {
                'term': row['city'],
                'location_types': 'airport',
                'limit': 1,
                'active_only': True
            }
            iata_response = requests.get(
                url="https://tequila-api.kiwi.com/locations/query",
                params=query,
                headers=header,
                )
            data = iata_response.json()
            iata_code = data['locations'][0]['city']['code']
            row_data = {
                    'city': row['city'],
                    'iataCode': iata_code,
                    'lowestPrice': row['lowestPrice']
                }

            requests.put(
                url=f'{self.endpoint}/{self.row_count}',
                headers=self.header,
                json=row_data)
            row_info = {
                'lowestPrice': row['lowestPrice'],
                'iataCode': row['iataCode']
                }
            self.route.append(row_info)
            self.row_count += 1
        return self.route
