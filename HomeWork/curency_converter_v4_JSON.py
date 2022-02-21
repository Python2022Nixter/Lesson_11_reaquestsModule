import pathlib
import requests
import json
import datetime


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
check_from_currency = False
check_to_currency = False
check_amount = False
searched_rates = {}

def input_data_to_convert():
    global from_currency
    global to_currency
    global amount
    global check_from_currency
    global check_to_currency
    global check_amount
    while not check_from_currency:
        from_currency = input("From currency: ").upper()
        try:
            if find_rate(from_currency):
                print(f"{from_currency} rate: {find_rate(from_currency)}")
            check_from_currency = True
            pass
        except:
            print("Wrong currency")
            check_from_currency = False
            pass
        pass

    while not check_to_currency:
        to_currency = input("To currency: ").upper()
        try:
            if find_rate(to_currency):
                print(f"{to_currency} rate: {find_rate(to_currency)}")
            check_to_currency = True
            pass
        except:
            print("Wrong currency")
            check_to_currency = False
            pass
        pass
    while not check_amount:
        amount = input("Amount: ")
        try:
            amount = float(amount)
            check_amount = True
            pass
        except:
            print("Wrong amount")
            check_amount = False
            pass
        pass
    return from_currency, to_currency, amount


def find_rate(currency):
    rates = json.loads(all_rates.text)["rates"]
    return rates[currency]


input_data_to_convert()
res = find_rate(to_currency) / find_rate(from_currency) * amount
print(f"{amount} {from_currency} = {res:0.2f} {to_currency}")

# save to file

FILE_NAME = "search_results.json"
path = pathlib.Path(__file__).parent.joinpath(FILE_NAME)

# TODO: save to JSON file.........
def read_from_file(path):
    with open(path, "r") as f:
        data = json.load(f)
        pass
    return data
def save_to_file(path, data):
    with open(path, "w") as f:
        json.dump(data, f)
        pass
    pass

def set_dict():
    out = {
        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"): {
        amount: [from_currency, to_currency],
        "result": res
        }
    }
    return out
try:
    searched_rates = read_from_file(path)
    # print(searched_rates)
except:
    print("File is empty")
searched_rates.update(set_dict())
save_to_file(path, searched_rates)