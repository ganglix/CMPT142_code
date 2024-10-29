# Write a Python function that accepts string parameter s and
# prints whether s has an even or odd amount of characters.
# Sample function console output:
# "Dog" has an odd number of characters.

def check_even(s):
    """
    check if a string contains even or number of characters, and print the result.
    :param s: string, string to be checked
    :return: None
    """
    if len(s) % 2 == 0:
        print(f"{s} contains even number of characters.")
    else:
        print(f"{s} contains odd number of characters.")