# recursion
# "the family chain of new phones"


# problem solving - delegation metaphor
# 1 find the base case (easy)
# 2 find a way to reduce the problem (not easy): reduce steps of procedure, quantity of a number, size of a list
# 3 find the relationship between the solution of the reduced problem and the original problem


def is_even(n):
    """ returns True if n (non-negative) is an even number,
    otherwise return False.
    """
    # base case
    if n == 0:
        return True
    elif n == 1:
        return False
    else:
        # recursive case : delegated work is to determine if n-2 is even
        is_n_minus_2_even = is_even(n-2) # True or False
        # n would be the same result true/false as n-2
        return is_n_minus_2_even

print(is_even(5))

"""flowtrace is_even(5)
is_even(5)
n = 5
if 5 == 0
elif 5 == 1
is_n_minus_2_even = is_even(5-2)
                    n = 3
                    if 3 == 0
                    elif 3 == 1
                    is_n_minus_2_even = is_even(3-2)
                                        n = 1
                                        if 1 == 0
                                        elif 1 == 1
                                        return False
                    is_n_minus_2_even =  False
                    return False                   
is_n_minus_2_even = False                    
return False

"""
def is_even_ver2(n):
    """ returns True if n (non-negative) is an even number,
    otherwise return False.
    """
    # base case
    if n == 0:
        return True
    # elif n == 1:    # this base case merged to recursive case
    #     return False
    else:
        # recursive case : delegated work is to determine if n-1 is even
        is_n_minus_1_even = is_even(n-1) # True or False
        # n would be the opposite result true/false as n-1
        return not is_n_minus_1_even

print(is_even_ver2(6))


# recursion depth
for n in range(int(1e5)):
    print(f'large number{n}', is_even_ver2(n))  # after 5984, it stopped printing as max number of function calls reached!
