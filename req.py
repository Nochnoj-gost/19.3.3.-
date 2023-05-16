import json

import requests

status = 'available'

# res = requests.get(url, headers=headers, params=params)
res = requests.get( f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", headers = {'accept': 'application/json'})
print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

# res = requests.post(url, headers=headers, data=data)   data — это данные, отправляемые на сервер в теле запроса. Передаются в формате словаря data = {‘key1’: ‘value1’, ‘key2’: ‘value2’}.
data = {"id": 2365, "category": { "id": 2365,  "name": "string" },  "name": "doggie",  "photoUrls": ["string"], "tags": [{ "id": 2365, "name": "string" }],  "status": "available" }
data = json.dumps(data)
headers = {'accept': 'application/json',  "Content-Type" : "application/json"}
res1 = requests.post( f"https://petstore.swagger.io/v2/pet", headers = headers, data = data)
print(res1.status_code)
print(res1.text)
print(res1.json())
print(type(res1.json()))

# res = requests.put(url, data=data)
data = {"id": 2365, "category": { "id": 2365,  "name": "string" },  "name": "doggie-boss",  "photoUrls": ["string"], "tags": [{ "id": 2365, "name": "string" }],  "status": "available" }
data = json.dumps(data)
headers = {'accept': 'application/json',  "Content-Type" : "application/json"}
res2 = requests.put(f"https://petstore.swagger.io/v2/pet", headers = headers, data = data)
print(res2.status_code)
print(res2.text)
print(res2.json())
print(type(res2.json()))

# res = requests.delete(url, **kwargs)
headers = {'accept': 'application/json'}
res3 = requests.delete(f"https://petstore.swagger.io/v2/pet/2365", headers=headers)
print(res3.status_code)
print(res3.text)
print(res3.json())
print(type(res3.json()))

