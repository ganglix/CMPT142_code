# demo1
# Tower Name Location
# Tokyo Skytree Japan
# Canton Tower China
# CN Tower Canada

tower = {
    "Tokyo Skytree": "Japan",
    "CN Tower": "Canada",
    "Canton Tower": "China",
}


# Let’s modify the dictionary:
# (a) Remove the entry whose location is "Canada"
# for tower_name in tower:
#     print(tower[tower_name])

# for country in tower.values():  this is not recommended.

for tower_name in tower.copy():   # do not iterate over a size-changing dict
    if tower[tower_name] == "Canada":
        # remove this record
        tower.pop(tower_name)


# (b) Add a new entry with tower name "Eiffel Tower" and
# location "Paris"
tower["Eiffel Tower"] = "Paris"


# (c) Oops! Update the tower entry "Eiffel Tower" to have
# location "France"
tower['Eiffel Tower'] = "France"




