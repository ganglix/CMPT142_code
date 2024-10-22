
#    _______
#    7654321
#    0123456
s = "Fiction"
# print(
#     s[1:3], # ic
#
#     s[-4:10],  # step is 1. [-4, -3,...0...1, 2, ...9]
#                # when the index(+/-) is mixed type. focus on position
#                # -4-> t   10-> right boundary n
#
#     s[0:len(s):2], # Fcin
#
#     type(s[0:len(s):-1]), # does not make sense, -> empty string ''
#
#     '--------',
#
#     s[len(s):-8:-1] # backwards
#
# )


#    ___________
#    BA987654321
#    0123456789A        note: A is 10    B is 11
s = "Green Arrow"

# (a) the first five characters of s, i.e. "Green"
print(s[0:5])

# (b) the fourth to eighth characters of s inclusive, i.e. "en Ar"
print(s[3:7+1])

# (c) the last five characters of s, i.e. "Arrow"
print(s[-5:])
print(s[6:])

# (d) every third character of s from the second character
# onwards, i.e. "rnrw"
print(s[1::3])

# (e) the last five characters of s in reverse, i.e. "worrA".
print(s[-1:-5-1:-1])
print(s[:-6:-1])
last_five = s[-5:]
print(last_five[::-1])
print('xxxx')
print(s[-5:][::-1])