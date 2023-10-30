#Using if and elif to set conditions to check the age
#Display a message to show its appropriate age group

age = 1

if age<2:
    print("the indivual is a baby")
elif age>=2 and age<4:
    print("the indivual is a toddler")
elif age>=4 and age<13:
    print("the indivual is a kid")
elif age>=13 and age<20:
    print("the indivual is a teenager")
elif age>=20 and age<65:
    print("the indivual is a adult")
elif age>=65:
    print("the indivual is a elder")