#Gather the sum of marks from 5 different subjects
#print out the average of the marks
math_Marks = int(input("Insert marks of Math : "))
english_Marks = int(input("Insert marks of English : "))
chem_Marks = int(input("Insert marks of Chemistry : "))
physics_Marks = int(input("Insert marks of Physics : "))
bio_Marks = int(input("Insert marks of Biology : "))
Average = (math_Marks + english_Marks + chem_Marks + physics_Marks + bio_Marks) / 5
print(Average)