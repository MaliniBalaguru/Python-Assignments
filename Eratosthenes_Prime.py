# Sieve of Eratosthenes
import math
# Create list to numbers from 2 to n
number = int(input("Enter any number : "))
primes_list = []
for prime in range(2, number + 1):
    primes_list.append(prime)
#print(primes_list)
#for numbers from 2 to square root of input number
prime = 2
while prime <= math.sqrt(number):
    if prime in primes_list:                                #if number exists in primes_list,
        for multiple in range(prime*2,number+1,prime):      #all of it's multiples in primes_list have to be deleted
            if multiple in primes_list:
                primes_list.remove(multiple)
    prime +=1

print(primes_list)



