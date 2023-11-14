#Using loop, print out the values in the dictionary
personal_Information = {
    "Name" : "Gian"
    ,
    "Last Name" : "Akiat"
    ,
    "Age" : 18
    ,
    "Day of bith" : 3
    ,
    "Month of birth" : "August"
    ,
    "Year of birth" : 2005
    }
for information in personal_Information.values():
    print(information)