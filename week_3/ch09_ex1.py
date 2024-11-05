# Write Python code which asks a user to input a string from
# the console until it is identical to pre-defined string passcode.
# When this occurs, print the number of attempts made to
# enter the correct string. e.g. "3 attempt(s) made."

passcode = "cmpt142"
# for the first time, ask user to input
user_input = input("Enter your password: ")
count = 1
# start checking
while user_input != passcode:
    # keep asking user to input
    user_input = input("Wrong Password! Try again: ")
    count += 1

# when the user get the correct passward
print(f"{count} attempts made")

