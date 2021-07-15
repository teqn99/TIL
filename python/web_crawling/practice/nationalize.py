import requests

name = 'yoon'
url = f'https://api.nationalize.io/?name={name}'
response = requests.get(url).json()

print(response)

country_list = []
for i in range(len(response['country'])):
    country_list.append(response['country'][i]['country_id'])
print(country_list)

country_pred = country_list[0]
print(country_pred)