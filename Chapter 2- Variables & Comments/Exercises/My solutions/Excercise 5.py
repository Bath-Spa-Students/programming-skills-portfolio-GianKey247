wallet = 50
USB = 6
Number_of_USB = int(wallet/USB)
change = wallet - (Number_of_USB* USB)
print(f"The number of USB that she can buy is {Number_of_USB}")
print(f"The change that she will have is {change}")