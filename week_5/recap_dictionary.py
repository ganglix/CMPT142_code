# count vowel letters in a string

def vowel_counter(s):
    """
    count the vowels in a string
    :param s: str, a string to be counted
    :return: dict, count of vowels in a string
    """
    count_result = {}
    # iterate over all chars, # do this for all chars
    for char in s:
        # check if that chat is a vowel
        if char in 'aeiou':
        # if it is, then count it
            if char not in count_result:
                # initialize the count record
                count_result[char] = 0
            # then, anyways add 1
            count_result[char] += 1
    return count_result

print(vowel_counter('apple'))


tempts = [[1,2,3], # Jan
          [4,5,6], # Feb
          [7,8,9]  # Mar
          ]

for i in range(len(tempts)):
    tempt_month = tempts[i]
    month_avg = sum(tempt_month)/len(tempts)

month_avg_list = []
for tempt_month in tempts:
    month_avg = sum(tempt_month)/len(tempts)
    month_avg_list.append(month_avg)

month_avg_list = [sum(tempt_month)/len(tempts) for tempt_month in tempts]

