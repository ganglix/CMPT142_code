a = 3
b = 4
c = 5

print(
    (a+b > c) or not (a > c and a > b)
)






# One more thing
def i_was_called():
    print("I was called")
    print('cmpt'[100])


if True or i_was_called():
    print('done')
