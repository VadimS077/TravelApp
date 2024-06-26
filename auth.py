import requests
import uuid
import os
from dotenv import load_dotenv


class Authorizator:

    def __init__(self):
        self.__authURL = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
        self.token = self.__get_token()

    @staticmethod
    def load_data():
        env_path = os.path.join(os.path.dirname(__file__), '.env')
        if os.path.exists(env_path):
            load_dotenv(env_path)
        else:
            print('Warning: no environment variable found!')

    def __get_token(self):

        myuuid = str(uuid.uuid4())

        self.load_data()
        secret = os.environ.get('AUTH_DATA')

        payload = {
            'scope': 'GIGACHAT_API_PERS'
        }

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'RqUID': myuuid,
            'Authorization': f'Bearer {secret}'
        }
        resp = requests.post(self.__authURL, data=payload, headers=headers, verify=False)
        tk = resp.json()['access_token']
        return tk