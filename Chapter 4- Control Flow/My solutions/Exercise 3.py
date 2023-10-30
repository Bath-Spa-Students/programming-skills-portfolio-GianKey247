#Using if statements, set a variable and check the variable if it passes the condition
#Make a seperate if statement where the variable doesnt pass the condition
#if alien color is green give 5 points, if yellow give 10 points, if red give 15 point
#if statement to check the alien color and give different amount of points, depending on the alien color

alien_color = "Green"
points = 0
if alien_color == "Green":
    points = points + 5
elif alien_color == "Yellow":
    points = points + 10
elif alien_color == "Red":
    points = points + 15
else:
    print("You missed")
print(f"You earnt {points} points")

alien_color = "Yellow"

points = 0
if alien_color == "Green":
    points = points + 5
elif alien_color == "Yellow":
    points = points + 10
elif alien_color == "Red":
    points = points + 15
else:
    print("You missed")
print(f"You earnt {points} points")

alien_color = "Red"

points = 0
if alien_color == "Green":
    points = points + 5
elif alien_color == "Yellow":
    points = points + 10
elif alien_color == "Red":
    points = points + 15
else:
    print("You missed")
print(f"You earnt {points} points")