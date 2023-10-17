Names = ["migz","ola","nathan","laiba","aya"]
messages = ['he will say "make it stop" when you have a problem',
            'she good',
            'sensable compared the rest of them',
            'she has more work experience compared to the rest of us',
            'she is always sleepy']

#another method
#count =len(Names)
#for index in range(count):
#    print(Names[index],messages[index])

for index, name in enumerate(Names):
    print(Names[index],messages[index])