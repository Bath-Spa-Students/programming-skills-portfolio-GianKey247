#Using a list, store sandwich orders
#Move the elements in one list to another
#Using a loop, reomave all instances of a specific element in the list
#Use a for loop to display a message that you are working on the sandwich
#Use for loop to display the finished sandwich list

sandwich_orders = ["pastrami", "Ham", "Chicken", "pastrami", "Beef", "Cheese", "pastrami"]
finished_sandwiches = []

#Removes all  'pastrami' inside the list
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

#Displays the message and moves elements from one list to another
while sandwich_orders:
    current_making_sandwich=sandwich_orders.pop()
    print(f"i am working on your {current_making_sandwich} sandwich")
    finished_sandwiches.append(current_making_sandwich)

for finished_sandwich in finished_sandwiches:
    print(f'Eat your {finished_sandwich} sandwiches')