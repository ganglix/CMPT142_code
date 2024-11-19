"""
Exercise 1:
Apply the algorithm-pseudocode-code workflow:
Given a list of numbers, compute how many
numbers are above the average

Algorithm:
Calculate the total value of the list of numbers
calculate the average of the list of number
count how many numbers are above the average

Pseudocode:
Create a function: aboveAverage()
parameters: a list of numbers
return: number of numbers above the average

initialize total = 0
for every number in the list
    add the number to total

average = total / number of numbers in the list

initialize count = 0
for every number in the list
    if that number > average
        count = count + 1
count is the number of numbers above the average

"""

# code
def aboveAverage(L):
    """
    calculate the number of numbers above the average of a list
    :param L: list, a list of numbers
    :return: int, number of numbers above the average
    """

    # calculate average
    total = 0

    for number in L:
        total += number

    average = total / len(L)

    # count the number of numbers above average
    count = 0
    for number in L:
        if number > average:
            count = count + 1
    return count

print(aboveAverage([1, 2, 3, 4, 5]))