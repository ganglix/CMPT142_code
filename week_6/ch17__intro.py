# Search algorithm

# search for a number from a list of numbers


# linear search
def linear_membership_search(c, target_key):
    """
    a linear membership search for the target key

    c:          a sequence of numbers or strings
    target_key: the target key for the search
    return: True if target key is in the collection
    """
    # base case
    if len(c) == 0:
        return False
    # elif len(c) == 1:      This base case is included in the recursive cas3
    #     if c[0] == target_key:
    #         return True
    #     else:
    #         return False
    else:
        # recursive case, reduce the length to reduce the problem
        # remove the first number and shorten the list
        if c[0] == target_key:
            return True
        else:
            # search the rest shortened list
            return linear_membership_search(c[1:], target_key)


# print(linear_membership_search([1,2,3], 0))




# binary search

def binary_membership_search(c, target_key):
    """
    A binary membership search function
    :param c: list, collection of data, sorted by its search keys
    :param target_key: target key to search for
    :return: True if target key is in the collection
    """
    if len(c) == 0:
        return False
    else:
        mid_index = len(c) // 2
        # check the middle number
        if c[mid_index] == target_key:
            return True
        else:
            if c[mid_index] > target_key:
                # check the left side
                left = c[:mid_index]
                return binary_membership_search(left, target_key)
            else:
                right = c[mid_index:]
                return binary_membership_search(right, target_key)


# generate an array to work with
import numpy as np
c = np.random.uniform(0,9, size=5).astype(int)
c.sort()
print(f"is 1 in {c}? {binary_membership_search(c, 1)}")
