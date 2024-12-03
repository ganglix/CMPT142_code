# Write a recursive function to find the smallest value in a list of
# numbers.


# 1 base case
# 2 recursive case (reduced problem, how to reduce)
# 3 relationship between the problem and the reduced problem

def smallest(L):
    """
    returns the smallest number of a list of numbers
    :param L: list, a list of numbers
    :return: int or float, the smallest number in the list L
    """
    # base case
    if len(L) == 0:
        return None
    elif len(L) == 1:
        return L[0]

    # recursive case (reduced problem)
    # remove the first item to shorten the list
    smallest_short_list = smallest(L[1:])

    # relationship between the problem and the reduced problem
    if L[0] < smallest_short_list:
        return L[0]
    else:
        return smallest_short_list

print(smallest([1,2,3,0,4,5]))

def smallest_ver2(L):
    """
    returns the smallest number of a list of numbers
    :param L: list, a list of numbers
    :return: int or float, the smallest number in the list L
    """
    # base case
    if len(L) == 0:
        return None
    elif len(L) == 1:
        return L[0]

    # recursive case (reduced problem)
    # cut the list into half to shorten the list
    mid_index = len(L)//2
    left_half_list = L[0: mid_index]
    right_half_list = L[mid_index :]

    smallest_left_half = smallest_ver2(left_half_list)
    smallest_right_half = smallest_ver2(right_half_list)

    # relationship between the problem and the reduced problem
    if smallest_left_half < smallest_right_half:
        return smallest_left_half
    else:
        return smallest_right_half