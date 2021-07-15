import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/'
response = requests.get(url).text
data = BeautifulSoup(response, 'html.parser')
yen = data.select_one('#worldExchangeList > li.on > a.head.jpy_usd > div > span.value')
print(yen)
result = yen.text

print(f'현재 엔/달러 환율은 {result}엔/1달러 입니다.')