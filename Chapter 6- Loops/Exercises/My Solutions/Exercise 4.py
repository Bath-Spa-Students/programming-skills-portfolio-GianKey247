#Using a list, store sandwich orders
#Move the elements in one list to another
#Use a for loop to display a message that you are working on the sandwich
#Use for loop to display the finished sandwich list

sandwich_orders = ["Ham", "Chicken", "Beef", "Cheese"]
finished_sandwiches = []

#Displays the message and moves elements from one list to another
while sandwich_orders:
    current_making_sandwich = sandwich_orders.pop()
    print(f"i am working on your {current_making_sandwich} sandwich")
    finished_sandwiches.append(current_making_sandwich)

for finished_sandwich in finished_sandwiches:
    print(f'Eat your {finished_sandwich} sandwiches')