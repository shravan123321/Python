# write the python program to check if a number is a prime or not
# Python program to check if a number is prime or not

num = int(input("Enter the number: "))
isprime = True

if num <= 1:
    isprime = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            isprime = False
            break

if isprime:
    print("The number is prime.")
else:
    print("The number is not prime.")