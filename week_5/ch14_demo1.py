# Read in the file data to create dictionary extensions that
# maps extension numbers to employees

# open
# absolute path: full directory
# file_path = r"C:\Users\gal894.STPETERS\Desktop\CMPT142_lecture_code\week_5\ext_directory_data.txt"

# relative path
# . means current folder of your code
# .. means parent folder that contains your code

# relative_path = './ext_directory_data.txt'
# relative_path = '../week_5/ext_directory_data.txt'

# by default, python use current folder as path
file_name = 'ext_directory_data.txt'  # in current folder of your code

# open file
f = open(file_name, 'r')  # r means read mode, the returned f is the handle
extensions = {} # ext: name
# read line
for line in f:
    line = line.rstrip()  # at the end of each line there  is a invisible newline "\n", we want to get rid of
    # parse the line string with ,
    # get the record
    line = line.split(',')  # now the line is a list of strings
    # put these records to the dict
    extensions[int(line[0])] = line[1]

print(extensions)

# close file, easy to forget!
f.close()