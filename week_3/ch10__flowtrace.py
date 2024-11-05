# flowtrace

# flowtrace

L = [1, 2, 3, 4, 5, 6]
for value in L:
    L.remove(value)
print(L)

"""
L = [1, 2, 3, 4, 5, 6]
for value in [1, 2, 3, 4, 5, 6]
    value = 1  # first item in [1, 2, 3, 4, 5, 6]
    [1, 2, 3, 4, 5, 6].remove(1)
    value = 3 # second item in [2, 3, 4, 5, 6]
    [2, 3, 4, 5, 6].remove(3)
    value = 5 # third item in [2, 4, 5, 6]
    [2, 4, 5, 6].remove(5)
print([2, 4, 6])
"""





L = []
for i in range(3):
    L.append([])
for char in "abc":
    L[0].append(char)
print(L)

"""
L = []
for i in range(3)
    i = 0
    [].append([])
    i = 1
    [[]].append([])
    i = 2
    [[], []].append([])
for char in "abc":
    char = 'a'
    [[], [], []][0].append('a')
    char = 'b'
    [['a'], [], []][0].append('b')
    char = 'c'
    [['a', 'b'], [], []][0].append('c')
print([['a', 'b', 'c'], [], []])

"""

L = []
for i, char in zip(range(3), "abc"):
    L.append([char])
print(L)