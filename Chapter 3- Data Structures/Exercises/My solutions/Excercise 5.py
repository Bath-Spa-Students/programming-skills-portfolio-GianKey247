#List out the names, you would like to invite to a dinner party
#Print out a personalised message for each element
#Replace one element in the guest list and print out the updated guest list

#list of names
Names = ["rick astley", "Takehito Koyasu", "mark hamil"]
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
