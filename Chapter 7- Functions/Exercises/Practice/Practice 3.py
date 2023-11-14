#make a function, set a perameter
#check if the paremeter is a prime number or not
def is_prime(num):
    if num == 1:
        return "Not a prime number"
    for prime in range(2,num):
        if (num % prime) == 0:
            return "Not a prime number"
    return "prime number"

print(is_prime(29))

