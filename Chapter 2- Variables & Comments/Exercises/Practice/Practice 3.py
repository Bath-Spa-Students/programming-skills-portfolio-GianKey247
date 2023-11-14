#assign different variables with different data types
#print out a string containing all the variables
fruit = input("Input a fruit : ")
number = int(input(f"How many {fruit} do you want? : "))
price = float(input(f"what is the price of the {fruit} : "))
seller = input(f"from who you baught the {fruit} from ? : ")
money = int(input(f"How much did you give to {seller}? : "))
print (f"You baught {number} {fruit} with the price of {price} from {seller} which you gave {money}")
