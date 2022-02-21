# currency from
# curremcy to
# amount to convert
# print result

# save online data to JSON file

import requests
import json


API_KEY = "4585446990311ad17f3ff45442c24766"
URL_STRING = f"http://api.exchangeratesapi.io/v1/latest?access_key={API_KEY}"


# Step 1:
def get_rates():
    rates = requests.get(URL_STRING, headers={"User-Agent": "XY"})

    return rates


all_rates = get_rates()
from_currency = ""
to_currency = ""
amount = ""

# Step 2 Input data from console: FROM, TO, AMOUNT


def input_data_to_convert():
    global from_currency
    global to_currency
    global amount
    from_currency = input("From currency: ").upper()
    to_currency = input("To currency: ").upper()
    amount = float(input("Amount to convert: "))
    return from_currency, to_currency, amount

# STEP 3: find the rate for the currency


def find_rate(currency):
    rates = json.loads(all_rates.text)["rates"]
    return rates[currency]

# STEP 4: convert the amount & print the result


input_data_to_convert()
res = find_rate(to_currency) / find_rate(from_currency) * amount
print(f"{amount} {from_currency} = {res:0.2f} {to_currency}")
