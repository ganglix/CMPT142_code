# creating functions: parameter, arguments, return, (scope)
def addition(par1, par2):
    result = par1 + par2
    return result

answer = addition(1,2)
print(answer)
"""
answer = addition(1,2)
--------inside function, under the hood, not visible from outside---------
par1 = 1
par2 = 2
result = 1 + 2
return 3
----------------------------------------
answer = 3
print(3)

"""