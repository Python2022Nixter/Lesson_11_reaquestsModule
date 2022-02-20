# currency from
# curremcy to
# amount to convert
# print result

# save online data to JSON file

import pathlib
import requests
import json


API_KEY = "4585446990311ad17f3ff45442c24766"
URL_STRING = f"http://api.exchangeratesapi.io/v1/latest?access_key={API_KEY}"

rates = requests.get(URL_STRING, headers={"User-Agent": "XY"})
EUR = json.loads(rates.text)["rates"]["EUR"]
USD = json.loads(rates.text)["rates"]["USD"]
ILS = json.loads(rates.text)["rates"]["ILS"]

print(f"EUR: {EUR}, USD: {USD}, ILS: {ILS}")
# convert ILS to USD
res = ILS / USD
print(f"Shekel {ILS} / in {USD} = {res:0.2f}")
print(f" 100 dollars in ILS = {100 * res:0.2f}")

FILE_NAME = "rates.json"
path = pathlib.Path(__file__).parent.joinpath(FILE_NAME)

with open(path, "w") as f:
    json.dump(json.loads(rates.text), f)
    pass

# Step 1:
def get_rates():
    
    
    return None

all_rates = get_rates()

# Step 2 Input data from console: FROM, TO, AMOUNT
def input_data_to_convert():
    from_currency = input("From currency: ")
    to_currency = input("To currency: ")
    amount = float(input("Amount to convert: "))
    return from_currency, to_currency, amount

# STEP 3: 