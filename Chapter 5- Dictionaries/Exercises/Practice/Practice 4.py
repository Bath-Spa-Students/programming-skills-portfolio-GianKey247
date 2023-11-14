#Using loop, print out the keys and values in the dictionary
#print out a sentence
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
for information_Key in personal_Information.keys():
    print(f"My {information_Key} is {personal_Information[information_Key]}")