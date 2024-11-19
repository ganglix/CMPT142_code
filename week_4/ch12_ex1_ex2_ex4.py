def is_valid_username(username):
    """
    determines if username meets these constraints:
    - 1-18 characters long
    - can be letters and/or numbers
    - underscore is allowed if it’s not the first character
    username: string to check validity of
    return: True if username satisfies constraints
    """

# Testing - black box
# black box reason: check if the function does what it is supposed to do. If the function does what it promises in the docstring
# to have a good coverage of the functionality of the function.

# test cases
# Test cases that test the length requirement is satisfied

# • Length is between 1-18 characters
"""
inputs: ""
expected_outputs: False # figure out this by looking at the docstring, do the calulation on your own
reason: Length is 0 characters; does not satisfy constraints of length

inputs: "a"
expected_outputs: True # figure out this by looking at the docstring, do the calulation on your own
reason: Length is exactly 1; it satisfies constraints of length, also does not violate other constraints

inputs: "_"
expected_outputs: False # figure out this by looking at the docstring, do the calulation on your own
reason: Length is exactly 1; but it is not valid because _ is the first character

inputs: "a"*18
expected_outputs: True # figure out this by looking at the docstring, do the calulation on your own
reason: Length is exactly 18; and it is valid

inputs: "a"*19
expected_outputs: False # figure out this by looking at the docstring, do the calulation on your own
reason: Length is 19; exceeding 18
"""

# can be letters and/or numbers
"""
inputs: "@"
expected_outputs: False  # figure out this by looking at the docstring, do the calulation on your own
reason: special characters "@", not valid

inputs: "0"
expected_outputs: True
reason: 0 is a number, and satisfies other constraints

inputs: "a"
expected_outputs: True
reason: "a" is a letter, and satisfies other constraints too.

inputs: "a0"
expected_outputs: True
reason: "a0" has both number and letter, and satisfies other constraints too.

inputs: "é"
expected_outputs: True
reason: Non standard English letter is a letter
"""


#     - underscore is allowed if it’s not the first character
"""
inputs: "_a"
outputs_expected: False
reason: "_a" has a leading _, which is not valid

inputs: "a_a"
outputs_expected: True
reason: "a_a" has _ in the middle, and satisfies other constraints.

inputs: "a_"
outputs_expected: True
reason: "a_" has _ in the end, and satisfies other constraints
"""


# test driver example
# test driver is a program that runs the test cases

# one example for one test case
inputs = "a_"
outputs_expected = True
reason = '"a_" has _ in the end, and satisfies other constraints'
# outputs from the funtion
outputs = is_valid_username(inputs)

# compare
# if outputs == outputs_expected:   # no need to notify if the test case is passed, no news is good news
#     print("Pass")
if outputs != outputs_expected:
    print(f"Fail for this test case"
          f"inputs: {inputs}"
          f"expected:{outputs_expected}"
          f"function returned: {outputs}"
          f"test reason: {reason}")   # this reason is help message for later debugging

















# # ~~~~~~~~~~~~~~~~after dictionary~~~~~~~~~~~~~~~~~~~~
#
# # dictionary of test case suite to feed into test driver loop
# test_suite = [
#     # call for length -zero username (empty string)
#     {"inputs": [""],
#      "outputs": False,
#      "reason": "length must be be 1-18 characters"},
#
#     # call for length -one username of invalid character
#     {"inputs": ["+"],
#      "outputs": False,
#      "reason": "username can only contain letters , numbers , underscores"},
#
#     # call for length -one username of a letter
#     {"inputs": ["a"],
#      "outputs": True,
#      "reason": "username is allowed to have letters"},
#
#     # call for length -18 username of numbers only with trailing underscore
#     {"inputs": ["0" * 17 + "_"],
#      "outputs": True,
#      "reason": "username is allowed to have numbers and trailing underscore"},
#
#     # call for length -three username with letter , number , underscore
#     {"inputs": ["a_0"],
#      "outputs": True,
#      "reason": "username is allowed to have letters , numbers , underscore"},
#
#     # call for length -three username with letter , number , starting underscore
#     {"inputs": ["_a0"],
#      "outputs": False,
#      "reason": "can’t start with underscore"},
#
#     # call for length -18+ username of letters and numbers
#     {"inputs": ["a0" * 18],
#      "outputs": False,
#      "reason": "can’t have more than 18 characters"}
# ]
#
# # a generic loop for test drivers
# # the inputs are in a list , so it has to be modified
# for test in test_suite:
#     inputs = test["inputs"]
#     result = is_valid_username(inputs[0])
#
#     if result != test["outputs"]:
#         print(f"Testing fault: is_valid_username () returned {result} on inputs {inputs}"
#               f"\ntest reason: {test['reason']})\n")
