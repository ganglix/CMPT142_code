s = 'fire'
L = [1, 2, 3]
L2 = [ [1 , 2] , [3 , 4] ]

print(L + [4, 5, 6])
print(L + [s])
print(L + L2)
print(L*3)
print("fir" in s)  # x in y returns a boolean value
print(1 in L2) # because the entry in L2 are sublists
print(1 in L2[0])  # True, 1 in [1 , 2]
print(1 in L2[0:1]) # False, 1 in [ [1 , 2] ]
print(L2[0:1])  # slicing of a list of lists creates a list of sublist(s)
