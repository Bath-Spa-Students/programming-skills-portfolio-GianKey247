#Using a list, add dictionaries containing information of a individuals pet
#Use For loop to display the key and values in the dictionaries

pets = []

persons_Pet1 = {
    'Owner': 'Pater'
    ,
    'Pet Name': 'Cotton'
    ,
    'Pet type': 'Dog'
    ,
    'Species': 'Samoyed'
}
pets.append(persons_Pet1)
persons_Pet2 = {
    'Owner': 'Carla'
    ,
    'Pet Name': 'Stick'
    ,
    'Pet type': 'Lizard'
    ,
    'Species': 'Bearded Dragon'
}
pets.append(persons_Pet2)
persons_Pet3 = {
    'Owner': 'Michigen'
    ,
    'Pet Name': 'Iguazu'
    ,
    'Pet type': 'Cat'
    ,
    'Species': 'American shorthair'
}
pets.append(persons_Pet3)


for pet in pets:
    for key, value in pet.items():
        print(f'The {key} is {value}')
    print()    