Names = ["rick astley", "Takehito Koyasu", "mark hamil"]
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
