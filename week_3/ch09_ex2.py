# Write a Python program that uses a for-loop to print all
# integers between 300 and 600 (inclusive) that are divisible
# by both 3 and 5. Print how many of these numbers were
# found

count = 0
for number in range(300, 600+1):  # 600 included
    if number % 3 == 0 and number % 5 == 0:
    # if number % 15 == 0 :
        print(number)
        count += 1
print(f"{count} numbers found")
print(1/6.28)