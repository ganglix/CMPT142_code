# Up until now, only immutable data types have been passed
# as arguments to functions. What happens when we pass
# mutable data?
# Let us observe the effect on an input variable before,
# during, and after a function call that changes the value.

def appendage(minilist, x):
    minilist.append(42)
    x = x + 5


L = [10, 20, 30]
x = 50
appendage(L, x)
print(L)
print(x)




# -----------------------------------------
# # does this operation create a new list?

