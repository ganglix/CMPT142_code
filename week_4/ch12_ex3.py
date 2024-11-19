def is_valid_password(password):
    """
    determines if password meets these constraints:
    - 9-18 characters long
    - no Underscores or minus _,-
    password: string to check validity of
    return: True if password satisfies constraints
    """
    is_valid = True

    if len(password) < 9 or len(password) > 18:
        is_valid = False
        return is_valid
    if "_" in password:
        is_valid = False
        return is_valid
    if "-" in password:
        is_valid = False
        return is_valid

    return is_valid


# Testing - white box
# reasoning: To have FULL coverage of the code. Every single line should be run at least once.

"""
inputs: "a"*8 # You should look at the code
expected_outputs: False # Important: we do not trust the code, because we are testing it. 
                        # We should still hand calculate it by understanding its functionality from docstring ONLY
reason: password length less than 9; Trigger line 11, if statement to be True  # code coverage

inputs: "_a"
expected_outputs: False  # by reading the docstring
reason: Trigger line 14, if statement to be True; therefore the block of code under it will be covered  # code coverage

inputs: "a-"  # by looking at the code in line 17
expected_outputs: False   # by look at the docstring
reason: Trigger line 17, if-statement to be True, so the block of code under it will be covered.

"""