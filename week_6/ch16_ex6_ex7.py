"""
N   F(N)
0   1
1   3
2   5
3   7    F(3) = F(2) + 2
4   9    F(4) = 9 = F(3) + 2
5   11   F(5) = 11 = F(4) + 2
----------------------------
F(n) = F(n-1) + 2
"""

def F(n):
    # base case
    if n == 0:
        return 1
    else:
        # recursive case: F(n-1)
        delegated_result = F(n-1)

        # find F(n) based on the result of F(n-1): F(n) = F(n-1) + 2
        final_result = delegated_result + 2

        return final_result


