# CMPT 142 - Sorting Algorithms
# contains implementations of sorting algorithms from the readings:
#  - merge sort
#  - quick sort


#########################
# MERGE SORT
#########################
def merge(S1, S2):
    """
    combines two sorted sequences into single sorted sequence
    S1: sorted sequence to combine
    S2: other sorted sequence to combine
    return: single sorted sequence of S1, S2 combined
    """
    # let S be an empty sequence
    S = []
    # repeatedly move the smallest item to S
    while len(S1) > 0 and len(S2) > 0:
        if S1[0] < S2[0]:
            S.append(S1[0])
            del S1[0]
        else:
            S.append(S2[0])
            del S2[0]
    # once one of S1 or S2 is empty, append the remaining
    # non-empty sequence to S.
    if len(S1) > 0:
        S.extend(S1)
    else:
        S.extend(S2)
    return S



def merge_sort(S):
    """
    merge sort a list in ascending order and return it
    :param S: a list to be sorted
    :return: sorted list
    """
    # base case
    if len(S) <= 1:
        return S
    else:
        # divide step
        left = S[0 : len(S)//2]
        right = S[len(S)//2 : ]

        # recursive solving
        left_sorted = merge_sort(left)
        right_sorted = merge_sort(right)

        # conquer step
        return merge(left_sorted, right_sorted)




#########################
# QUICK SORT
#########################

def quick_sort(S):
    """
    quick sort a list and return it
    :param S: a list to be sorted
    :return: sorted list
    """
    if len(S) <= 1:
        return S
    else:
        # pivot = any item of S # e.g. the last item of S
        pivot = S[-1]
        L = []
        G = []
        E = []
        # L = items in S smaller than pivot
        # G = items in S larger than pivot
        # E = items in S equal to the pivot
        for item in S:
            if item < pivot:
                L.append(item)
            elif item == pivot:
                E.append(item)
            else:
                G.append(item)
        # recursively solve the sub -problems of sorting L and G
        L_sorted = quick_sort(L)
        G_sorted = quick_sort(G)

    return L_sorted + E + G_sorted  # (where + represents concatenation)