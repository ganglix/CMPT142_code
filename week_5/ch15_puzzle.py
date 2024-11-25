import numpy as np

# Create a signed 8-bit integer array
# with the single data item 10.
x = np.array([10]).astype('int8')

# x[0] starts at 10 and gets larger with each loop iteration.
# Is this In infinite loop?

while x[0] > 0:
    x[0] = x[0] + 1
    print(x[0])