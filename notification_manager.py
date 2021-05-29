import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


class NotificationManager:
    def __init__(self, message: str):
        self.msg_body = message
        self.account_sid = os.environ['ACCOUNT_SID']
        self.auth_token = os.environ['AUTH_TOKEN']
        self.proxy_client = TwilioHttpClient()
        self.client = Client(self.account_sid, self.auth_token)

    def send_message(self):
        """Sends an SMS to personal number"""
        self.client.messages.create(
            body=self.msg_body,
            from_=os.environ["TWILIO_PHONE_NUMBER"],
            to=os.environ["MY_PHONE_NUMBER"]
        )
