Names = ["Golf","Mclaren F1","Supra","Skyline","Ford GT"]
messages = ['is going to my main car of chice for daily means',
            'is the best track car that i would like to drive atleast once',
            'is one of the best tuner cars out there but its extremely rare and expensive',
            'have a similar case to the supra',
            'is one of my favourite child hood cars']

#another method
#count =len(Names)
#for index in range(count):
#    print(Names[index],messages[index])

for index, name in enumerate(Names):
    print(Names[index],messages[index])
