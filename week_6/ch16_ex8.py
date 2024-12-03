"""
N   F(N)
0   1
1   2
2   4
3   7
4   11   F(4) = F(3) + 4
5   16   F(5) = F(4) + 5

F(n) = F(n-1) + n
"""


def F(n):
    # base case
    if n == 0:
        return 1
    else:
        # recursive case: F(n-1)
        delegated_result = F(n - 1)

        # find F(n) based on the result of F(n-1): F(n) = F(n-1) + n
        final_result = delegated_result + n

        return final_result

print(F(4))
