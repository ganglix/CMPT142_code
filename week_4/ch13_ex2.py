# Exercise 2

# Suppose we have dictionary availability:
# keys: friend’s name
# values: list of days they are available to play a game
# (a) Write a function that accepts an availability dictionary and returns a new dictionary mapping days to
# friends who can play that day.
# (b) Using the function from a):
# Find the day most friends can attend to play the game
# List who can and can not attend the session that day

availability = {"Neo":      ["Monday"],
                "Morpheus": ["Sunday"],
                "Smith":    ["Monday", "Tuesday"]}

def scheduler(availability):
    """
    Convert a dictionary of availability to a dictionary of schedule
    :param availability: dict, name: list of available days
    :return: dict, day: list of available names
    """
    # initialize schedule {day: list of available names}
    schedule = {}

    # check for all names, one by one
    for name in availability:
        # get their available days (a list of day(s))
        days = availability[name]

        # check for each day
        # add the record to schedule, by appending their name to the list of available names for that day
        for that_day in days:
            if that_day not in schedule:  # {day: list of available names}
                schedule[that_day] = []   # initalize an empty list to be appended later
            schedule[that_day].append(name)
    return schedule

schedule = scheduler(availability)
print(schedule)
# find the day that most friends can attend
day_with_max_ppl = ''
max_number_ppl = 0

for day in schedule: # schdule {day: list of names}
    ppl_list = schedule[day]
    if len(ppl_list) > max_number_ppl:
        max_number_ppl = len(ppl_list)
        day_with_max_ppl = day

print(max_number_ppl, 'are available on', day_with_max_ppl)

for name in availability:
    if name not in schedule[day_with_max_ppl]:
        print(name, 'is not available')

# use list comprehansion to crate a list of ppl who can not attend the max ppl day event

not_attend = [name for name in availability if name not in schedule[day_with_max_ppl]]