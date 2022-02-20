"""
customer_id ; customer_first_name ; customer_second_name ; customer_mail ; customer_phone1 ; customer_phone2 ; customer_city ; customer_country ; customer_orderdate ; customer_orderamount ; customer_orderstatus 
1; Fox ; Hyde ; pretium.et@condimentum.net ; 673-35-716-25-87 ; 090-58-956-22-86 ; Chicago ; San Marino ; 28.10.21 ; $2578.12 ; ordered 


"""
from email import header


str1 = "customer_id ; customer_first_name ; customer_second_name ; customer_mail ; customer_phone1 ; customer_phone2 ; customer_city ; customer_country ; customer_orderdate ; customer_orderamount ; customer_orderstatus "
str2 = "1; Fox ; Hyde ; pretium.et@condimentum.net ; 673-35-716-25-87 ; 090-58-956-22-86 ; Chicago ; San Marino ; 28.10.21 ; $2578.12 ; ordered "


def convert_string_to_customer(customer_data_list: list[str], headers_list: list[str]) -> dict[str, dict]:
    next_customer_key = customer_data_list[3].strip()
    customer = {
        next_customer_key: {
            headers_list[0].strip(): int(customer_data_list[0].strip()),
            "name": {
                headers_list[1].strip(): customer_data_list[1].strip(),
                headers_list[2].strip(): customer_data_list[2].strip()
            },
            headers_list[3].strip(): {
                "name": customer_data_list[3].strip().split("@")[0],
                "domain": customer_data_list[3].strip().split("@")[1]
            },
            "tel": {
                headers_list[4].strip(): customer_data_list[4].strip(),
                headers_list[5].strip(): customer_data_list[5].strip()
            },
            headers_list[6].strip(): customer_data_list[6].strip(),
            headers_list[7].strip(): customer_data_list[7].strip(),
            # headers_list[8].strip(): customer_data_list[8].strip().split("."),
            headers_list[8].strip(): {
                "day":customer_data_list[8].strip().split(".")[0],
                "month":customer_data_list[8].strip().split(".")[1],
                "year":customer_data_list[8].strip().split(".")[2]
                },
            headers_list[9].strip(): float(customer_data_list[9].strip().replace("$", "")),
            headers_list[9].strip(): customer_data_list[5].strip()
        }
    }

    return customer

"""
Testing data
headers_test = str1.split(";")
customer_test = str2.split(";")
print(convert_string_to_customer(customer_test, headers_test))
"""