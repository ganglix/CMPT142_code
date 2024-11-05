# while vs. for
# In this demonstration, we’ll see a situation where using a
# while-loop is preferable to using a for-loop.

# password example

passcode = "cmpt142"
# for the first time, ask user to input
user_input = input("Enter your password: ")
count = 1
max_try = 3
# ask user to input when the passward is wrong and user did not exceed the max trials
while user_input != passcode and count < max_try: # once max_try is reached, no more prompt
    # keep asking user to input
    user_input = input("Wrong Password! Try again: ")
    count += 1

# when the loop is done, there are ONLY two outcomes
# 1 user typed in correct passcode
if user_input == passcode:
    print(f"{count} attempt(s) made")
# if count == max_try:   # no need
else: # max exceeded
    print(f"maximum number of trials exceeded, you are locked out. Forget your password?")


