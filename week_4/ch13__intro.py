# dictionary {key : value, key1 : value1}, Those records or pairs are not ordered

# KEYS

# VALUES

phone_book = {"Gang" : "3068888888",
              "Tristan" : "3061111111"}

# what type of data can be a dictionary key
# any immutable data can be a dict key
# we can not have duplicate keys; key should be unique

# add record
print(phone_book)
print(phone_book["Gang"])  # lookup
phone_book['Abdul'] = "3060000000" # add record
print(phone_book)

# remove record
phone_book.pop("Gang")
print(phone_book)

# look-up
phone_book['Abdul'] = "3069999999"
print(phone_book)

if "Gang" in phone_book:
    print(phone_book["Gang"])
else:
    print("not found")

# Whatever you do to a dict, you do it through keys!!

phone_book.get("Gang", "return this message if Gang is not in phone_book") # not required

# value can also be a dict

address_book = {"Gang": {"phone nubmer": "3068888888",
                         "email": "gang.li@usask.ca"},

                "Gang1": {"phone nubmer": "3068888888",
                         "email": "gang.li@usask.ca"}
                }

print(address_book)

# WHen work with dict, always be clear: what is the key, what is the value!!