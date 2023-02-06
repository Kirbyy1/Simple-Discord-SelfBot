import requests
import uuid
import random


random_user_agent = random.choice(requests.get(
    'https://gist.githubusercontent.com/pzb/b4b6f57144aea7827ae4/raw/cf847b76a142955b1410c8bcef3aabe221a63db1/user-agents.txt').text.split(
    '\n'))


# 401 = Bad auth token
# 429 = Rate Limit

class Discord:
    MESSAGES = "https://discord.com/api/v9/channels/{channel_id}/messages"
    JOIN_SERVER = "https://discord.com/api/v9/invite/{invite_code}"

    FRIEND_LIST = "https://canary.discord.com/api/v8/users/@me/relationships"
    CHANNELS = "https://discord.com/api/v9/users/@me/channels"

    def __init__(self, token: str, **kwargs):
        self.proxy: str = kwargs.get('proxy', {})

        if not isinstance(token, str):
            raise ValueError(f'The authentication token must be a string not a {type(token)}')

        user_agent: str = kwargs.get('user_agent',
                                     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari')

        self.headers = {
            'authorization': token,
            'content-type': 'application/json',
            'cache-control': 'no-cache',
            'user-agent': user_agent,
        }

    def send_message(self, channel_id: str | int, message: str | int):
        URL: str = self.MESSAGES.format(channel_id=channel_id)
        guid: str = str(uuid.uuid4())
        # tts = Text to speech
        payload = {'content': message, 'tts': False, 'nonce': guid[:15]}

        return requests.post(url=URL, headers=self.headers,
                             json=payload, proxies=self.proxy)

    def read_messages(self, channel_id: str):
        URL: str = self.MESSAGES.format(channel_id=channel_id)
        return requests.get(url=URL, headers=self.headers, proxies=self.proxy)

    def delete_message(self, channel_id: str | int, message_id: str | int):
        URL: str = f'{self.MESSAGES.format(channel_id=channel_id)}/{message_id}'
        return requests.delete(url=URL, headers=self.headers, proxies=self.proxy)

    def join_server(self, invite_code: str):
        URL = self.JOIN_SERVER.format(invite_code=invite_code)
        return requests.post(url=URL, headers=self.headers, proxies=self.proxy)

    def get_friends(self):
        URL = self.FRIEND_LIST
        return requests.get(URL, headers=self.headers)

    def get_channels(self):
        URL = self.CHANNELS
        return requests.get(URL, headers=self.headers)


