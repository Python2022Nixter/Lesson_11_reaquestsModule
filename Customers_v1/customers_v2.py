import pathlib
from my_csv_tools import convert_string_to_customer as converter

FILE_NAME = "customers.csv"
path_to_file = pathlib.Path(__file__).parent.joinpath(FILE_NAME)
# with CSV module

customers_dict = {}  # all customer
with open(path_to_file) as f:
    customers_headers = f.readline()
    customers_list = f.readlines()
    pass

for next_customer_string in customers_list:
    customers_dict.update(converter(next_customer_string.split(";"), customers_headers.split(";") ))   
    
    pass

print(F"{customers_dict['Phasellus.dolor.elit@lectus.co.uk']['tel']}")
# print(customers_dict.keys())


# for next_key in customers_dict.keys():
#     print(F"{next_key}")
#     print(F"{customers_dict[next_key]['name']['customer_first_name']} {customers_dict[next_key]['name']['customer_second_name']}")
#     #print(customers_dict[next_key])
#     # print email
#     print(F"{customers_dict[next_key]['customer_mail']['name']}@{customers_dict[next_key]['customer_mail']['domain']}")
#     print("")
#     pass

for next_item in customers_dict.items():
    print(F"{next_item[0]}")
    print(F"{next_item[1]['name']['customer_first_name']} {next_item[1]['name']['customer_second_name']}")
    #print(customers_dict[next_key])
    # print email
    print(F"{next_item[1]['customer_mail']['name']}@{next_item[1]['customer_mail']['domain']}")
    print("")
    pass

for k, v in customers_dict.items():
    print(F"{k}")
    print(F"{v['name']['customer_first_name']} {v['name']['customer_second_name']}")