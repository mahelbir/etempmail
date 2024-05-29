import requests

from etempmail.TempMailException import TempMailException


class TempMail:
    id = None
    email = None
    recovery = None

    def __init__(self, recovery: str = None, url: str = 'https://etempmail.com', debug_response: bool = True):
        self.debug_response = debug_response
        self.url = url
        self.__session = requests.session()
        self.__headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.8',
            'origin': self.url,
            'priority': 'u=1, i',
            'referer': self.url + '/',
            'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            'x-kl-ajax-request': 'Ajax_Request',
            'x-requested-with': 'XMLHttpRequest',
        }
        if recovery:
            self.recover(recovery)
        else:
            self.__get_email()

    def __get_email(self):
        response = self.__session.post(f'{self.url}/getEmailAddress', headers=self.__headers)
        try:
            json = response.json()
            self.id = int(json['id'])
            self.email = json['address']
            self.recovery = json['recover_key']
        except Exception:
            raise TempMailException('get_email', 'request', response, self.debug_response)

    def inbox(self) -> list:
        response = self.__session.post(f'{self.url}/getInbox', headers=self.__headers)
        try:
            json = response.json()
            return json
        except Exception:
            raise TempMailException('inbox', 'request', response, self.debug_response)

    def recover(self, recovery: str):
        if recovery:
            response = self.__session.post(f'{self.url}/recoverEmailAddress', headers=self.__headers, data={
                'key': recovery
            })
            try:
                json = response.json()
            except Exception:
                raise TempMailException('recovery', 'request', response, self.debug_response)
            if not json['success']:
                raise TempMailException('recovery', 'key', response, self.debug_response)
        self.__get_email()

    def change(self):
        response = self.__session.post(f'{self.url}/deleteEmailAddress', headers=self.__headers)
        if response.status_code != 200:
            raise TempMailException('change', 'request', response)
        self.__get_email()
