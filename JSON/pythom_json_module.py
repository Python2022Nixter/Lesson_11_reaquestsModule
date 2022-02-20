from array import array
from ipaddress import ip_address
import json
from operator import le
import pathlib

str = """
[{"id":1,"first_name":"Arvie","last_name":"Zamboniari","email":"azamboniari0@ask.com","ip_address":"64.18.94.154"},
{"id":2,"first_name":"Alice","last_name":"Tuny","email":"atuny1@senate.gov","ip_address":"235.36.217.131"},
{"id":3,"first_name":"Roger","last_name":"Bauchop","email":"rbauchop2@bing.com","ip_address":"41.121.193.93"},
{"id":4,"first_name":"Jaquenette","last_name":"Catterson","email":"jcatterson3@opensource.org","ip_address":"163.253.47.15"}]
"""

str2 = """
{
    "John doe" :
    {
        "user_name": "String value",
        "age": "Number value",
        "user_email": {
            "name": "String value",
            "domen": "String value"
        },
        "courses": [
            "Web", "Android", "iOS"
        ],
        "payed": true,
        "class": "String value"
    },

    "Nixter" :
    {
        "user_name": "String value",
        "age": "Number value",
        "user_email": {
            "name": "String value",
            "domen": "String value"
        },
        "courses": [
            "Web", "Android", "iOS"
        ],
        "payed": true,
        "class": "String value"
    }
    
}


"""

json_from_string = json.loads(str) # convert string to object
print(type(json_from_string))
print(type(json_from_string[3]))

print(json_from_string[0].keys())
print(json_from_string[0].values())
print(json_from_string[0].items())
print()
json_from_string2 = json.loads(str2)
print(json_from_string2.keys())
print(json_from_string2.values())
print(json_from_string2.items())
print()
print(json_from_string2["Nixter"].keys())

user_dict1 = {"id":1,"first_name":"Arvie","last_name":"Zamboniari","email":"azamboniari0@ask.com","ip_address":"64.18.94.154"}
str_from_json = json.dumps(user_dict1) # convert object to string
print(type(str_from_json), str_from_json)

FILE_NAME = "user_dict1.json"
path = pathlib.Path(__file__).parent.joinpath(FILE_NAME)
with open(path, "w") as f:
    json.dump(user_dict1, f)
    pass

FILE_NAME = "persons_v1.json"
path = pathlib.Path(__file__).parent.joinpath(FILE_NAME)
with open(path) as f:
    json_string_form_file = f.read()
    pass

persons = json.loads(json_string_form_file)
print(type(persons), len(persons))
print(persons[0].keys())
print(persons[0].values())
print(persons[0]["ip_address"])

FILE_NAME = "persons_v1_new.json"
path = pathlib.Path(__file__).parent.joinpath(FILE_NAME)
with open(path, "w") as f:
    json.dump(persons, f, indent=4)
    pass