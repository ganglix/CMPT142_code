# Indexing and Slicing of !Sequences!
# str
'CMPT 142'
# list
print(['C','M',123])
print([])

# tuple
print( (1,2) )
print((1,'one'))

# •What is indexing used for?
# •What does a positive index mean?
# •What does a negative index mean?

#         ________
#         87654321
# index   01234567
course = 'CMPT 142'
print('~'*20)
print(course[0])
print(course[-1])
print(course[7])
print(len(course))
print(course[len(course)-1])



# --------- take a break -----------

# •What is slicing used for?
# •What are the meanings of the First, second, and third
# numbers in a slicing operation?
text = 'computer science'
print(text[0:8:1])  # [start: stop(not included): step]
print(text[0:3])  # by default, the step is one when step is omitted
print(text[:3])   # by default, start from boundary (left boundary)
print(text[len(text)-1 :  : -1])   # by default, end at boundary (left boundary, 0 is included)

print(text[:])
print(text[::])
print(text[::-1]) # same as print(text[len(text)-1 :  : -1])
#         [                    .....]

text = 'computer science'
print(text[3:1000])  # out of range index -> boundary

# I want to mention omitted value, index out of range, and range of slice
