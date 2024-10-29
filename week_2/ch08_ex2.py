a = False
b = False
c = True

print(
    not b, # True
    c and b, # False
    a or b, # False
    not b and c, # True
    b or not c,  # False
    b and c or a, # False
    c or b and a  # bonus True   # NAO
)

# be redundant: c or (b and a)