Names = ["Rick astley", "Takehito Koyasu", "Mark hamil", "Mi", "Yu"]
message = '*insert dinner invitation message here*'

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

print("Due to me being a massive moron, i didnt know that i had no table for the party and so, i must remove people from the guest list, down to 2 people")
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