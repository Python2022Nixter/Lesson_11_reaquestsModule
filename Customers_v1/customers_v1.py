import pathlib
import csv


FILE_NAME = "customers.csv"
path_toFile = pathlib.Path(__file__).parent.joinpath(FILE_NAME)

customers_dictionary = {}
with open(path_toFile) as file:
    
    scv_reader = csv.DictReader(file, delimiter=";")
    for row in scv_reader:
        next_customer = {}
        for key, value in row.items():
            next_customer[key.strip()] = value.strip()
        #next_customer = {key.strip(): value.strip() for key, value in row.items()}
        customers_dictionary[next_customer["customer_mail"]] = next_customer
        pass
    pass


print("customers_dictionary")  
print(len(customers_dictionary))
print(customers_dictionary["sed.facilisis@rutrumjusto.net"])