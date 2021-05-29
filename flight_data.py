class FlightData:
    def __init__(self, destination: dict):
        self.destination = destination

    def show_flight_data(self):
        """Combines data from FlightSearch class in more readable way and returns the message"""
        message = f"Low price alert! Only €{self.destination['price']} to fly from " \
                  f"{self.destination['city-from']}-{self.destination['airport-from']} " \
                  f"to {self.destination['city-to']}-{self.destination['airport-to']}, " \
                  f"from {self.destination['date-from']} to {self.destination['date-to']}"
        return message
