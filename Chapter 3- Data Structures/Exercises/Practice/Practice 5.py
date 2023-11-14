#in the list provided
#remove one instance of "20"
#Replace it with "200"
list1 = [5, 10, 15, 20, 25, 50, 20]
if 20 in list1:
    list1.remove(20)
    list1.append(200)
print(list1)
