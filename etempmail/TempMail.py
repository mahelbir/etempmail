from requests import session
from json import loads as json_decode
from etempmail.TempMailException import TempMailException


class TempMail:
    id = 0
    email = ''
    recovery = ''

    def __init__(self, recovery: str = None):
        self.__session = session()
        self.__headers = {
            'accept': 'application/json',
            'accept-language': 'tr,en-US;q=0.9,en;q=0.8,tr-TR;q=0.7',
            'origin': 'https://etempmail.com',
            'referer': 'https://etempmail.com/',
            'sec-ch-ua': '"Opera GX";v="89", "Chromium";v="103", "_Not:A-Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 OPR/89.0.4447.64',
            'x-requested-with': 'XMLHttpRequest',
        }
        self.start(recovery)

    def start(self, recovery: str = None):
        if recovery:
            response = self.__session.post('https://etempmail.com/recoverEmailAddress', headers=self.__headers, data={
                'key': recovery
            })
            try:
                json = json_decode(response.content)
                if not json['success']:
                    raise TempMailException('recovery', 'key', response)
            except Exception:
                raise TempMailException('recovery', 'request', response)

        response = self.__session.post('https://etempmail.com/getEmailAddress', headers=self.__headers)
        try:
            json = json_decode(response.content)
            self.id = int(json['id'])
            self.email = json['address']
            self.recovery = json['recover_key']
        except Exception:
            raise TempMailException('start', 'request', response)

    def inbox(self) -> dict:
        response = self.__session.post('https://etempmail.com/getInbox', headers=self.__headers)
        try:
            json = json_decode(response.content)
            return json
        except Exception:
            raise TempMailException('inbox', 'request', response)
