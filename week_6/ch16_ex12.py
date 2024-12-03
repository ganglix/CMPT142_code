"""
generation  ancestor
n   bees(n)
0   1
1   1
2   2
3   3
4   5
5   8
6   13
------
bees(n) = bees(n-1) + bees(n-2)
"""

def bees(n):
    if n == 0 or n == 1:
        return 1
    else:
        return bees(n-1) + bees(n-2)

# n = range(20)
# import matplotlib.pyplot as plt
# plt.plot(n, [bees(i) for i in n])
# plt.show()

# import time
# start = time.time()
# bees(20)
# end = time.time()
# number_of_calls = 2 ** 20
# time_per_call = (end - start) /  number_of_calls
#
# print("For bees(60), it will take ",
#       2**60 * time_per_call/3600/24/365/100, " century.")

# use dict to take notes of solved cases
bees_n_cache = {}   # n: bees_efficient(n)
def bees_efficient(n):
    if n == 0 or n == 1:
        return 1
    else:
        # check if the solution has already done,
        # only call function the first time you see n
        if n not in bees_n_cache:
            result = bees_efficient(n-1) + bees_efficient(n-2)
            bees_n_cache[n] = result
        # return the updated cached value
        return bees_n_cache[n]

print(bees_efficient(60))