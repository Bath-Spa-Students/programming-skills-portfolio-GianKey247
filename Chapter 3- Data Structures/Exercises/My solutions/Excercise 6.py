#List out the names, you would like to invite to a dinner party and print out a personalised message for each element
#Replace one element in the guest list and print out the updated guest list 
#Remove elements in the guest list down to 2 elements
#Print out the updated guest list then remove all elements in the guest list, Print out the empty guest list

Names = ["Rick astley", "Takehito Koyasu", "Mark hamil", "Mi", "Yu"]
message = 'is invited to your dinner party'

#Original guest list
for name in Names:
    print(name.title() , message)
print()

#Guest cant arrive to the event and replaces
print(f"unfortunaley, {Names[1]} cant come to the event")
del(Names[1])
Names.insert(1, "gianni matragrano")
print()

#Updated guest list
for name in Names:
    print(name.title() , message)
print()

print("Dining Table is not going to arrive in time and so, i must remove people from the guest list, down to 2 people")
print()
Removed_Name = Names.pop()
print(f'{Removed_Name} *insert cancelation to dinner party message here*')

Removed_Name = Names.pop()
print(f'{Removed_Name} *insert cancelation to dinner party message here*')

Removed_Name = Names.pop()
print(f'{Removed_Name} *insert cancelation to dinner party message here*')
print("\nThe 2 people that are coming to the dinner party is:")

#Updated guest list
for name in Names:
    print(name.title() , message)
print()

del(Names[0])
del(Names[0])

print("The list is now empty")

print(Names)