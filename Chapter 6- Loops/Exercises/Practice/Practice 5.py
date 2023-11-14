#Using while, user will input a number
#print out the largest number when the loop is broken
user_Number = int(input("input a number : "))
highest_number = 0
while user_Number != 0:
    if user_Number >= highest_number:
        highest_number = user_Number
    user_Number = int(input("input a number (Enter '0' to  exit) : "))
print(highest_number)

