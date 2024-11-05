# Write a Python function that uses a for-loop to print the
# number of times each lowercase vowel (a,e,i,o,u) occurs in a
# string s. e.g. "piece" prints "a:0 e:2 i:1 o:0 u:0".

s = "piece"
# # e
# print('e:',s.count('e'), sep='')


def vowel_count(text):
    count_a = 0
    count_e = 0

    for c in text:
        if c == 'a':
            count_a += 1
        elif c == 'e':   # checking these letters are mutually exclusive
            count_e += 1
    print(f"a:{count_a} e:{count_e}")

vowel_count(s)