#Using if statements, set a variable and check the variable if it passes the condition
#Make a seperate if statement where the variable doesnt pass the condition

alien_color = "Green"

points = 0
#Checks if alien color is green
if alien_color == "Green":
    points = points + 5

print(f"You got {points} points, somehow")

#Checks if alien color is green, but the alien color is Yellow
alien_color = "Yellow"

points = 0
if alien_color == "Green":
    points = points + 5

