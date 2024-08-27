import requests

class GroupMeAPI:
    def __init__(self, api_token):
        self.api_token = api_token

    def send_message(self, message):
        url = f'https://api.groupme.com/v3/bots/post'
        headers = {'Content-Type': 'application/json'}
        data = {'bot_id': self.api_token, 'text': message}
        response = requests.post(url, headers=headers, json=data)
        return response.json()