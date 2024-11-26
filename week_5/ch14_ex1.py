# Topic(s): Reading Files
# read file and create a list of dictionaries to store data
# looks like this:
# scientists = [{"name": "Isaac Newton",
#                "birth_year": 1643,
#                "death_year": 1727},
#               {"name": "Albert Einstein",
#                "birth_year": 1879,
#                "death_year": 1955}]

scientists = []
file_name = './subfolder/scientists_data.txt'
f = open(file_name, 'r')
for line in f:
    line = line.rstrip()
    # parse the line
    line = line.split(',')   # Isaac Newton,1643,1727
    # create a record
    record_dict = {"name": line[0],
                   "birth_year": int(line[1]),
                   "death_year": int(line[2]),
                   "age_at_death": int(line[2]) - int(line[1])}
    # add record to list
    scientists.append(record_dict)

f.close()
print(scientists)

from pprint import pprint  # pretty print
pprint(scientists)