#Using dictionaries
#Store information of lessons that you have learnt and Use For loop to display its key and value
python_Lessons = {
    'String': 'It mainly contains characters, like the aplhabets'
    ,
    'Float': 'It contains numbers with decimals'
    ,
    'Integer': 'It contains only whole numbers'
    ,
    "F string": 'Allows functions to be placed in the string'
    ,
    "If statement": 'Uses conditions to check the input and use appropriate output'
}
for key , value in python_Lessons.items():
    print(key.title(),value)

for key in python_Lessons.keys():
    print(key.title(), python_Lessons[key])