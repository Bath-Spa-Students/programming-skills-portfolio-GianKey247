#User will input toppings for a pizza
#Use a list to store the toppings
#Print out the toppings using a for loop
toppings = []
users_Toppings = input("Enter your toppings: ")
while users_Toppings:
    toppings.append(users_Toppings)
    users_Toppings = input("Enter more toppings(enter quit to stop): ")
#user will be given a prompt to make the program stop and display the toppings
    if users_Toppings == "quit":
            for topping in toppings:
                print(f"your topping on your pizza are {topping}")
            break


# while users_Toppings != "quit":
#      toppings.append(users_Toppings)
#      users_Toppings = input("Enter more toppings(enter quit to stop): ")
# for topping in toppings:
#     print(f"your topping on your pizza are {topping}")