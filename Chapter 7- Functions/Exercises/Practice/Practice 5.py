#make a function, set a perameter
#check if the paremeter is a prime number
def is_prime(num):
    if num == 1:
        return ""
    for prime in range(2,num):
        if (num % prime) == 0:
            return ""
    return "prime number"

print(is_prime(5))