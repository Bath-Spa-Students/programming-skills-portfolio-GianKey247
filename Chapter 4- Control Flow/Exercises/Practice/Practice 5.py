#set a varable for the user to input a month
#using if elif and else
#check the month to see which seaon is it
Month = input("Enter month name here (Ex : November): ")
if Month == "March" or Month == "April" or Month == "May":
    print("It is spring")
elif Month == "June" or Month == "July" or Month == "August":
    print("It is Summer")
elif Month == "September" or Month == "October" or Month == "November":
    print("It is Autumn")
elif Month == "December" or Month == "January" or Month == "Febuary":
    print("It is Winter")
else:
    print("input invalid")
