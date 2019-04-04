import urllib3
import requests
from pyats.topology import Device


class Identity:
    def __init__(self, first_name: str, last_name: str, telephone: str):
        self._first_name = first_name
        self._last_name = last_name
        self._telephone = telephone

    def get_first_name(self) -> str:
        return self._first_name

    def get_last_name(self) -> str:
        return self._last_name

    def get_telephone(self) -> str:
        return self._telephone


class Credentials:
    def __init__(self, email: str, password: str, news_letter: str):
        self._email = email
        self._password = password
        self._news_letter = news_letter

    def get_email(self) -> str:
        return self._email

    def get_password(self) -> str:
        return self._password

    def get_newsletter(self) -> str:
        return self._news_letter


class UserRegistration:
    def __init__(self, identity: Identity, credentials: Credentials):
        self._identity = identity
        self._credentials = credentials

    def registration_response(self, device: Device) -> str:
        urllib3.disable_warnings()
        return requests.post(
            f"https://{device.connections.main.ip}//index.php?route=account/register",
            {
                "customer_group_id": "1",
                "firstname": self._identity.get_first_name(),
                "lastname": self._identity.get_last_name(),
                "email": self._credentials.get_email(),
                "telephone": self._identity.get_telephone(),
                "password": self._credentials.get_password(),
                "confirm": self._credentials.get_password(),
                "newsletter": self._credentials.get_newsletter(),
                "agree": "1",
            },
            verify=False,
        ).url
