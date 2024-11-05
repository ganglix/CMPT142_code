# Control Flow: Repetition
# what is a computer good at?
# repeat till what? when?

# while loop starts and stops according to a condition
## things I want to mention: condition boolean, if/while, keep checking(eg.)

# counting example : 1~5
# count = 1
# count += 1 # count = count + 1
# # keep going until count == 5

# count = 1
# while count <= 5:
#     # when true, keep doing this block of code
#     print('inside the loop', count)
#     count += 1
#
# print('when the loop is done, count: ', count)


# for : repeat over a sequence
# mention types of sequence: string, range, list, dict

s = 'cmpt142'
# for i in range(len(s)):
#     print(s[i])

for char in s:
    print(char)

L = ['red', 'green', 'blue']
for colour in L:
    print(colour)

for colour in L[0:2]:
    print(colour)


