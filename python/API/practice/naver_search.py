import requests

# naver 요청 보낼 때 필요한 것들
naver_client_id = '76305r3cOTGAS4CCV5W9'
naver_Client_secret = '4gju3J8Aah'
URL = 'https://openapi.naver.com/v1/search/shop.json?query='

headers = {
    'X-Naver-Client-Id': naver_client_id,
    'X-Naver-Client-Secret': naver_Client_secret
}

query = 'ps5'

product = requests.get(URL+query, headers=headers).json()['items'][0]
print(product)
product_name = product['title']
print(product_name)
product_price = product['lprice']
print(product_price)
product_link = product['link']
print(product_link)

message = f' {product_name}\n {product_price}\n {product_link}'
print(message)