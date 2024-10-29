# Define a Python function called format_price that:
# (a) Has two integer parameters, indicating the cost in dollars
# and cents of an item
# (b) Returns a single string in the format "$D.C".
# (c) Example: if called with arguments 9 and 99, the function
# should return the string $9.99

def format_price(dollar, cent):
    formated = '$' + str(dollar) + '.' + str(cent)
    return formated

formated_price = format_price(9, 99)
print(formated_price)

# follow up on types of functions

# with args, no return
def print_format_price(dollar, cent):
    """
    It takes two numbers as dollar and cents, and formatted it into $dollar.cent
    :param dollar: int, number of dollar
    :param cent: int, number of cents
    :return: str, formatted string
    """
    formated = '$' + str(dollar) + '.' + str(cent)
    print(formated)

def print_format_price_v2(dollar, cent):
    """
    It takes two numbers as dollar and cents, and print out the formatted $dollar.cent
    :param dollar: int, number of dollar
    :param cent: int, number of cent
    :return: None
    """
    formated = format_price(dollar, cent)
    print(formated)


# no args, no return
# def print_format_price_v3():
#     """ Prompts user to input two numbers as dollar and cent, and print out the formatted $dollar.cent
#     :return: None
#     """
#     dollar = input("enter dollar: ")
#     cent  = input("enter cent: ")
#     formated = format_price(dollar, cent)
#     print(formated)

# print_format_price_v3()

help(print_format_price)

print(print_format_price.__doc__)