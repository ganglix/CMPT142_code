# This demonstration shows you how to call methods on string objects.


# initialize some variables to play with
url = "www.engineering.usask.ca"

# find the location of the first period in the url
location = url.find('.')  # returns the index of the first occurrece of '.'
print(location)

# find the location of the second period
print(url.find('.', location + 1 ))
# short_url = url[location+1 :]
# print(short_url.find('.') + location +1)

# similar to .find(), we have .index()
print(url.index('.'))

# help(url.index)
# count the number of periods in the url
print(url.count('.'))


#----------------------------------------
s = ' CMPT 142 '
# remove white space
print(s.strip())  # remove all leading and trailing spaces
print(s.rstrip()) # remove trailing spaces
print(s.lstrip()) # remove leading space

# what if we want to remove all spaces
print(s.replace(' ', ''))

# ------------------------
# count the number of characters in the url after removing "www."
print(url.removeprefix('www.'))
print(url.lstrip('w.')) # w, and . are the things to be removed


# when are they useful?
print(url.upper())
print(url.lower())
print(url.title())

# strings are immutable, all these methods create a copy
print(url)
print(s)

# how do I know what kind of methods are out there? How do I know the syntax/usage?

print(dir(s))