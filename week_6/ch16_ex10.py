"""
S       F(S)
''       ''
’a’     ’a’
’ab’    ’ba’
’abc’   ’cba’
’abcd’  ’dcba’  F('abcd') = 'd' + F('abc')
--------------------------------------------
F(S) = S[-1] + F(S[:-1])
"""
def F(s):
    """
    Return the reversed string of s.
    """
    # base case
    if len(s) == 0:  # empty string
        return s
    else:
        # recursive case  by removing the last chat from the string to make it shorter
        return s[-1] + F(s[:-1])

print(F('abcd'))