# Topic(s): Writing Files
# store’s item inventory to write (no "stock" means not carried by store)

# expected output
# Healing Herb,Heals minor wounds,25,0.25,5
# Smoke Cloud,Creates distraction,65,1.15,

inventory = [
    {"name": "Healing Herb", "desc": "Heals minor wounds",
     "cost": 25, "weight": 0.25, "stock": 5},
    {"name": "Antidote Vial", "desc": "Cures poisonous wounds",
     "cost": 50, "weight": 1.25, "stock": 3},
    {"name": "Paralysis Herb", "desc": "Paralyzes enemy when thrown",
     "cost": 75, "weight": 0.35},
    {"name": "Smoke Cloud", "desc": "Creates distraction for escape",
     "cost": 65, "weight": 1.15},
    {"name": "Fairie Dust", "desc": "Casts light in the darkness",
     "cost": 100, "weight": 0.4, "stock": 3},
]

# create a file
f = open('inventory.txt', 'w')

# get the item information
for item in inventory:   # item is a diction
    # prepare the line of information to be written to a file
    # all info except for stock
    line_to_write = ','.join([ item['name'], item['desc'], str(item['cost']), str(item['weight']), ''])

    # handle stock
    if "stock" in item:
        line_to_write += str(item['stock'])

    f.write(line_to_write)
    f.write("\n")

f.close()


#  out of scope
with open("inventory.txt", "w") as f:
    for item in inventory:
        line_to_write = ','.join([ item.get('name', ''),
                                   item.get('desc', ''),
                                   str(item.get('cost', '')),
                                   str(item.get('weight', '')),
                                   str(item.get('stock', ''))])  # return 'stock' value,
                                                                 # if stock is not an available key
                                                                 # return ''
        f.write(line_to_write)
        f.write("\n")
