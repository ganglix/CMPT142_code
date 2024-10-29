# Flowtrace with function

# status = "Healthy"
# def set_status(s):
#     status = s
#
# set_status("Poisoned")
# print(status)
#
# """
# status = "Healthy"
# set_status("Poisoned")
# ----------different piece of paper, inside the function, not visible from outside------------------
# s = "Poisoned"
# status = "Poisoned"
# -------------------------------------------------------------------------
# print(Healthy)
# """

# status = "Healthy"
# def set_status(s):
#     return s
#
# status = set_status("Poisoned")
# print(status)

status = "Healthy"
def set_status(s):
    # global status   # DO NOT USE this, illegal
    status = s

set_status("Poisoned")
print(status)

#~~(things I want to mention: scope, return, dangerous thing to do)






# optional: global var can be SEEN from inside the func but can not be touched

