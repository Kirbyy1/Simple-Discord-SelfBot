import requests
import uuid



class Discord:
    
    MESSAGES: str = "https://discord.com/api/v9/channels/{channel_id}/messages"
    JOIN_SERVER: str = "https://discord.com/api/v9/invite/{invite_code}"
    CHANNELS: str = "https://discord.com/api/v9/users/@me/channels"

    def __init__(self, token: str, **kwargs) -> None:
        self.proxy: str = kwargs.get('proxy', {})

        if not isinstance(token, str):
            raise ValueError(f'The authentication token must be a string not a {type(token)}')

        user_agent: str = kwargs.get('user_agent',
                                     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari')

        self.headers: dict = {
            'authorization': token,
            'content-type': 'application/json',
            'cache-control': 'no-cache',
            'user-agent': user_agent,
        }

    def send_message(self, channel_id: str | int, message: str | int) -> requests.Response:
        URL: str = self.MESSAGES.format(channel_id=channel_id)
        guid: str = str(uuid.uuid4())
        # tts = Text to speech
        payload: dict = {'content': message, 'tts': False, 'nonce': guid[:15]}

        return requests.post(url=URL, headers=self.headers,
                             json=payload, proxies=self.proxy)

    def read_messages(self, channel_id: str) -> requests.Response:
        URL: str = self.MESSAGES.format(channel_id=channel_id)
        return requests.get(url=URL, headers=self.headers, proxies=self.proxy)

    def delete_message(self, channel_id: str | int, message_id: str | int) -> requests.Response:
        URL: str = f'{self.MESSAGES.format(channel_id=channel_id)}/{message_id}'
        return requests.delete(url=URL, headers=self.headers, proxies=self.proxy)

    def join_server(self, invite_code: str) -> requests.Response:
        URL: str = self.JOIN_SERVER.format(invite_code=invite_code)
        return requests.post(url=URL, headers=self.headers, proxies=self.proxy)

    def get_channels(self) -> requests.Response:
        URL: str = self.CHANNELS
        return requests.get(URL, headers=self.headers)

