#Use if statments to check the users age
#Display the price of the movie ticket, depending on the age
customers_Age = int(input("Enter your age here: "))
while customers_Age:
    if customers_Age<3:
        print("movie ticket is free")
        customers_Age = int(input("Enter your age here: "))
    elif customers_Age>=3 and customers_Age<12:
        print("movie ticket is $10")
        customers_Age = int(input("Enter your age here: "))
    elif customers_Age>=12:
        print("movie ticket is $15")
        customers_Age = int(input("Enter your age here: "))
    else:
        print("Age entered is invalid")
        customers_Age = int(f"Enter your age here: ")
