from requests import session, get
from json import loads as json_decode
from re import findall
from etempmail.TempMailException import TempMailException


class TempMail:
    id = None
    email = None
    recovery = None

    def __init__(self, recovery: str = None, url: str = 'https://etempmail.com', debug_response: bool = True):
        self.debug_response = debug_response
        self.url = url
        self.__session = session()
        self.__headers = {
            'accept': 'application/json',
            'accept-language': 'en-US',
            'origin': self.url,
            'referer': self.url,
            'sec-ch-ua': '"Not/A)Brand";v="99", "Opera";v="101", "Chromium";v="115"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0',
            'x-requested-with': 'XMLHttpRequest',
        }
        if recovery:
            self.recover(recovery)
        else:
            self.__get_email()

    def __get_email(self):
        response = self.__session.post(f'{self.url}/getEmailAddress', headers=self.__headers)
        try:
            json = json_decode(response.content)
            self.id = int(json['id'])
            self.email = json['address']
            self.recovery = json['recover_key']
        except Exception:
            raise TempMailException('get_email', 'request', response, self.debug_response)

    def domains(self) -> list:
        response = get(self.url, headers=self.__headers)
        if response.status_code != 200:
            raise TempMailException('domains', 'request', response, self.debug_response)
        else:
            return findall(r'<option value="(\d+)".*?>(.+?)</option>', response.text)

    def inbox(self) -> list:
        response = self.__session.post(f'{self.url}/getInbox', headers=self.__headers)
        try:
            json = json_decode(response.content)
            return json
        except Exception:
            raise TempMailException('inbox', 'request', response, self.debug_response)

    def recover(self, recovery: str):
        if recovery:
            response = self.__session.post(f'{self.url}/recoverEmailAddress', headers=self.__headers, data={
                'key': recovery
            })
            try:
                json = json_decode(response.content)
            except Exception:
                raise TempMailException('recovery', 'request', response, self.debug_response)
            if not json['success']:
                raise TempMailException('recovery', 'key', response, self.debug_response)
        self.__get_email()

    def change(self, domain_id: str | int = None):
        if not domain_id:
            response = self.__session.post(f'{self.url}/deleteEmailAddress', headers=self.__headers)
        else:
            response = self.__session.post(f'{self.url}/changeEmailAddress', headers=self.__headers, data={
                'id': domain_id
            }, allow_redirects=False)
        if (not domain_id and response.status_code != 200) or (domain_id and response.status_code != 302):
            raise TempMailException('change', 'request', response)
        self.__get_email()
