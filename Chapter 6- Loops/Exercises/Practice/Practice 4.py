#using loops, make a loop infinite
#break the loop when a certain condition is met
words = input("Put a word here : ")
word_bank = []
while words !="quit":
    word_bank.append(words)
    words = input("Put a word here (Type: quit to exit) : ")
for word in word_bank:
    print(word)

