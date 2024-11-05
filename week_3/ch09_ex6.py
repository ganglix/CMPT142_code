# Classify the loops in these Python excerpts as terminating
# (reaches an end) or infinite in nature:

# # (a) not an inf loop
# for x in range(100, 10, 10):
#     print(x * 5)

# (b) silent inf loop
# sum = 0
# i = 0
# while i < 10:
#     sum = sum + i


# (c) # inf loop
# x = 5
# goal = 16
# while x != goal:
#     x = x + 2

# go = True
# while go:
#     user_input = input("Enter an instruction:")
#     if user_input == "quit":
#         go = False
# print('loop is done')

# (d)
# divisor = 2
# dividend = 49
# while dividend % divisor != 0:
#     divisor = divisor + 1
#     print(divisor)

# def prime_checker(n):
#     divisor = 2
#     while n % divisor != 0:
#         divisor = divisor + 1
#     # when the loop is done
#     if divisor == n:
#         # print(n, 'is a prime number')
#         return True
#     else:
#         # print(n, 'is not a prime number, can be at least divided by', divisor)
#         return False
#
# for number in range(1000,10000):
#     if prime_checker(number):
#         print(number)


# (e)
low = -100
high = 100
msg = " Enter int between " + str(low) + " to " + str(high) + ":"
num = int(input(msg))
while num >= low or num <= high:
    num = int(input(msg))
