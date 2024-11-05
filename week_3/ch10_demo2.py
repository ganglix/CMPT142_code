# List msgs contains sublists of the form [msg,days old]:
# msgs = [ ["Forgot the recipe again! #nofood",3],
# ["such a gluten #food #fivestar",10] ]
# Use list comprehensions to:
# (a) create list food_msgs of messages containing "#food"
# (b) create a new copy of food_msgs where messages are
# appended with "#yawn"

# Topic : List Comprehensions
# DEMO
# list of social media messages as sublists ( message , days since posted )

msgs = [["Forgot the recipe again! #nofood", 3],
        ["such a gluten #food #fivestar", 10],
        ["International #Food day! Hooray!", 1],
        ["Apple pie is bestest food", 5],
        ["lunchtime? #food #craving hits again", 9]]

# (a) create list food_msgs of messages containing "#food"
food_msgs = []
for m in msgs:  # m is a sublist
    if "#food" in m[0].lower():  # m[0] is the text(the first item)
        food_msgs.append(m)
print(food_msgs)

# list comprehension
# [ something to be added to this list for item in oldlist if a condition is true]
food_msgs = [m for m in msgs if "#food" in m[0].lower()]
print(food_msgs)

# (b) create a new copy of food_msgs where messages are
# appended with "#yawn" to the message

food_msgs_yawn = [ [m[0] + "#yawn", m[1]] for m in msgs ]

print(food_msgs_yawn)