import requests, json

url = f'https://mindicador.cl/api/uf/2024'
response = requests.get(url)
data = json.loads(response.text.encode("utf-8"))
for item in data["serie"]:
    print(item["fecha"], item["valor"])