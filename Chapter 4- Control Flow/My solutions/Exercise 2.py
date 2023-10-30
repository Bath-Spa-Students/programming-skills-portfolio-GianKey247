#Using if statements, set a variable and check the variable if it passes the condition
#Make a seperate if statement where the variable doesnt pass the condition
#if alien color is green, give 5 points if not, give 10 points

alien_color = "Green"
#if statement to check the alien color
points = 0
if alien_color == "Green":
    points = points + 5
else:
    points = points + 10

print(f"You got {points} points")

alien_color = "Yellow"
#if statement to check the alien color
points = 0
if alien_color == "Green":
    points = points + 5
else:
    points = points + 10

print(f"You got {points} points")