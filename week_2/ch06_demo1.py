# Write a docstring for the following function definition (abs()
# returns the absolute value of a number):

def print_smaller_absolute(num1, num2):
    '''
    It takes two numbers and return the absolute value of the smaller one and print a message
    :param num1: int or float, first number to compare
    :param num2: int or float, second number to compare
    :return: int or float, absolution value of the smaller number
    '''
    small_abs = abs(min(num1, num2))
    print("Absolute value of smaller number: ", small_abs)
    return small_abs



# who cares about docstring!

# things not to do.
# engineering example?
# style

