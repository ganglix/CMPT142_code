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

# (a) Creates list light_pkgs of parcels that weigh less than 5
light_pkgs = []
for w in pkg_weights:
    if w <= 5:
        light_pkgs.append(w)
print(light_pkgs)

# (b) Removes parcels from pkg_weights that exceed 15 lbs
# for w in pkg_weights:  # DO NOT iterate over a size-changing list
#     if w > 15:
#         pkg_weights.remove(w)
# print(pkg_weights)

# for w in pkg_weights.copy():
#     if w > 15:
#         pkg_weights.remove(w)
# print(pkg_weights)

heavy_weight = []    # a list of item to be removed
for w in pkg_weights:
    if w > 15:
        heavy_weight.append(w)

for w in heavy_weight:  # this list is not changing during the for loop
    pkg_weights.remove(w)
print(pkg_weights)


# (c) Print the:
# • contents of light_pkgs in ascending order
# light_pkgs.sort()  # this will change the light_pkgs list
# print(light_pkgs)

print(sorted(light_pkgs))   # sorted function creates a sorted copy; original list is not changed
print(light_pkgs)

# • number of parcels in light_pkgs
print(len(light_pkgs))

# • number of parcels removed from pkg_weights
print(len(heavy_weight))




# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~things I want to mention
# Modifying list while iterating DO NOT DO IT
# don't change list if possible
# use a clone





