# lists and tuples

# create a list
L = [1, 2, 3]

# indexing and slicing, same as string, or other sequences
print(
    L[0],
    L[-1],
    L[1:3],
)
print(L * 2)
import numpy as np
arr = np.array([1, 2, 3])  # this is array
print(arr*2)

# methods
# add an item: .append(), .extend(), +
new_stuff = L.append(4)  # in-place change, L is changed with adding 4 to it
print(new_stuff)
print(L)

L.extend(['garbage1', 'garbage2'])  # same as using +
print(L)

# remove an item: .remove(), .pop(), del
L.remove('garbage1')
L.remove('garbage2')
print('before pop', L)
popped_out = L.pop()  # by default, pop out the last item, and return it
print('after pop',L)
print('popped out:',popped_out)

# locating an item: index()
L.append('four')
print(L)
print(L.index('four'))

# sorting: .sort()
L_random = [2, 1, 4, 3]
L_random.sort()  # ascending order, change in place, L_random is changed
print(L_random)

# let do an attempt to use .sort() without changing the old L
L_old = [2, 1, 4, 3]
L_new = L_old    # we simply add another name to the list stored in the memory

print('L_new:', L_new)
print('L_old',L_old)
L_new.sort()
print('after we use L_new.sort()')
print('L_new:', L_new)
print('L_old',L_old)



# let do an attempt to use .sort() without changing the old L
L_old = [2, 1, 4, 3]
L_new = L_old.copy()    # .copy() creates a clone of L_old, identical but a new list

print('L_new:', L_new)
print('L_old',L_old)
L_new.sort()
print('after we use L_new.sort()')
print('L_new:', L_new)
print('L_old',L_old)

# list is mutable ! more examples in flowtrace observations





