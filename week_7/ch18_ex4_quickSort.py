# Algorithm quickSort(S)
# # sorts sequence S using quick sort
# pivot = any item of S # e.g. the last item of S
# L = items in S smaller than pivot
# G = items in S larger than pivot
# E = items in S equal to the pivot
#
# # recursively solve the sub -problems of sorting L and G
# quickSort(L)
# quickSort(G)
#
# S = L + E + G # (where + represents concatenation)
# return S


def quick_sort(S):
    """
    quick sort a list and return it
    :param S: a list to be sorted
    :return: sorted list
    """
    if len(S) <= 1:
        return S
    else:
        # sorts sequence S using quick sort
        pivot = S[-1]
        # L = [item for item in S if item < pivot]
        # G = [item for item in S if item > pivot]
        # E = [item for item in S if item == pivot]
        L = []
        G = []
        E = []
        for item in S:
            if item < pivot:
                L.append(item)
            elif item > pivot:
                G.append(item)
            else:
                E.append(item)

        # recursively solve the sub -problems of sorting L and G
        L_sorted = quick_sort(L)
        G_sorted = quick_sort(G)

        S = L_sorted + E + G_sorted # (where + represents concatenation)
        return S


# print(quick_sort([5, 4, 3, 2, 1]))


