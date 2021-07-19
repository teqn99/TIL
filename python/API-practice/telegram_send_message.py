import requests

# 기본 설정
TOKEN = '1872188053:AAEpGiIP0vOE2xql8ah0WXzVm1z_Dgz8wtQ'
APP_URL = f'https://api.telegram.org/bot{TOKEN}'

# chat_id 가져오기
# https://api.telegram.org/bot1872188053:AAEpGiIP0vOE2xql8ah0WXzVm1z_Dgz8wtQ/getUpdates
UPDATES_URL = f'{APP_URL}/getUpdates'
response = requests.get(UPDATES_URL).json()
# print(response['result'])

chat_id = response.get('result')[0].get('message').get('chat').get('id')
print(f'id: {chat_id}')
text = '파이썬으로 보낸 메세지입니다.'

# https://api.telegram.org/bot1872188053:AAEpGiIP0vOE2xql8ah0WXzVm1z_Dgz8wtQ/sendMessage?chat_id=1876753815&text=%EB%B3%B4%EB%82%B4%EC%A7%80%EB%82%98%EC%9A%94?
message_url = f'{APP_URL}/sendMessage?chat_id={chat_id}&text={text}'
requests.get(message_url)
