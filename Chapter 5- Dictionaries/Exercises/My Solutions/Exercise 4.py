#Using dictionaries
#Store information of Rivers in different parts of the world
#Use For loop to display its key and value

Rivers = {
    'Amazon': 'South America'
    ,
    'Mississippi': 'United States'
    ,
    'Mekong': 'East Asia and Southeast Asia'
    ,
    "Nile": 'Northeastern africa'
    ,
    "Congo": 'Africa'
}
for key in Rivers.keys():
    print(f"The river, known as the, {key.title()} is located at {Rivers[key]}")
print(f"\nThe rivers in the data are:")
for river in Rivers.keys():
    print(river.title())

print(f"\nThe countries in the data are:")
for country in Rivers.values():
    print(country.title())