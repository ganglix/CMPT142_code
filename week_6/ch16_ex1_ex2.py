
# 3! =
# 2! =
# 1! =
# 0! =

def factorial_a(N):
    if N == 0:
        return 1
    else:
        return factorial_a(N - 1) * N




# (a) What is the condition for the base case?

# (b) What is the condition for the recursive case?

# (c) What problem is being delegated?

# (d) How is the solution to the delegated problem used?


def factorial_b(N):
    if N > 0:
        return factorial_b(N - 1) * N
    else:
        return 1



# which one is better?
