#List out loactions of interest
#Follow sorting instructions in the Excercise 7

Locations = ["Italy", "Egypt", "America", "England", "Japan"]
print(f"Original List of locations: {Locations}")

#Sorts elements in list as alphabetical order
sorted_Locations = sorted(Locations)
print(f"Sorted list of location: {sorted_Locations}")
print(f"Original list of locations: {Locations}")

#Reverses order of elements inside the list
reversed_Locations = sorted(Locations, reverse=True)
print(f"Reversed Sorted list of locations {reversed_Locations}")
print(f"Original list of locations: {Locations}")

#Reverses order of elements inside the list
Locations.reverse()
print(Locations)
#Using Reverse to undo the Reverse
Locations.reverse()
print(Locations)
#Sorts the list, alphabetically
Locations.sort()
print(Locations)
#Sorts the list, alphabetically and in reverse
Locations.sort(reverse= True)
print(Locations)
