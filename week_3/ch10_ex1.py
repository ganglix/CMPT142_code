# A given list called pkg_weights contains weights of parcels
# (in lbs) queued for shipping. Write Python code that:
# (a) Creates list light_pkgs of parcels that weigh less than 5
# lbs from pkg_weights
# (b) Removes parcels from pkg_weights that exceed 15 lbs
# (c) Print the:
# • contents of light_pkgs in ascending order
# • number of parcels in light_pkgs
# • number of parcels removed from pkg_weights

pkg_weights = [2, 6, 8, 34, 56, 67, 4, 2, 33]

# (a) Creates list light_pkgs of parcels that weigh less than 5 lbs
light_pkgs = []
for p in pkg_weights:
    if p < 5:
        light_pkgs.append(p)
print(light_pkgs)

# (b) Removes parcels from pkg_weights that exceed 15 lbs
# for p in pkg_weights:  # Big mistake: iterating over a size-changing list # DONT do it
#     if p > 15:
#         pkg_weights.remove(p)
# print("after removing pkg > 15lb: ", pkg_weights)


# # use index:
# for i in range(len(pkg_weights)):  # Big mistake: iterating over a size-changing list # DONT do it
#     if pkg_weights[i] > 15:  # not work
#         pkg_weights.remove(pkg_weights[i])
# print("after removing pkg > 15lb: ", pkg_weights)

# # marking strategy [worked!]
# # step 1
# # mark the heavy ones
# heavy_pkgs = []  # to be removed later
# for p in pkg_weights:
#     if p > 15:
#         heavy_pkgs.append(p)
#
# # step 2, remove the heavy ones
# for p in heavy_pkgs:
#     pkg_weights.remove(p)
# print(pkg_weights)

pkg_weights_clone = pkg_weights.copy()
for p in pkg_weights_clone:  # use a copy (clone) for iteration, which is not changed in the block
    if p > 15:
        pkg_weights.remove(p)
print("after removing pkg > 15lb: ", pkg_weights)


# (c) Print the:
# • contents of light_pkgs in ascending order
# light_pkgs.sort()
# print(light_pkgs)
print(sorted(light_pkgs)) # does not change the light_pkgs

# • number of parcels in light_pkgs
print(len(light_pkgs))

# • number of parcels removed from pkg_weights
# print(len(heavy_pkgs))  # with two- step method

# another way  # with copy method
print(len(pkg_weights_clone) - len(pkg_weights))






# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~things I want to mention
# Modifying list while iterating DO NOT DO IT
# don't change list if possible
# use a clone





