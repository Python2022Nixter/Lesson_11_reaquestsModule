import requests 
import json

# API KEY - 4585446990311ad17f3ff45442c24766
# https://httpbin.org/get

# http://dummy.restapiexample.com/api/v1/employees

# URL_STRING = "https://httpbin.org/get"
# res = requests.get(URL_STRING, headers={"User-Agent": "XY"})

# json_from_response = json.loads(res.text)
# print(type(json_from_response), json_from_response)

# URL_STRING = "http://dummy.restapiexample.com/api/v1/employees"
# res = requests.get(URL_STRING, headers={"User-Agent": "XY"})

# json_from_response = json.loads(res.text)
# print(type(json_from_response), json_from_response)

API_KEY = "4585446990311ad17f3ff45442c24766"
URL_STRING = f"http://api.exchangeratesapi.io/v1/latest?access_key={API_KEY}"
res = requests.get(URL_STRING, headers={"User-Agent": "XY"})

json_from_response = json.loads(res.text)
print(type(json_from_response), json_from_response)
print(json_from_response["rates"]["ILS"])