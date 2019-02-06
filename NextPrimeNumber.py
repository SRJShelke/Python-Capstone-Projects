#Next Prime Number : Have the program find prime numbers until the user chooses to stop asking for the next one.


def isprime(n):
    if n < 2: return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

primes = (i for i in range(1000) if isprime(i))
prime_num = list(primes)
choice = "Y"
count= 0
while (choice!='N'):
	if choice == "Y":
		choice = input("Next?(Y/N)")
		if count < 100 :
			print(prime_num[count])
			count = count+1
	else :
		choice =input("Please Enter the correct input (Y/N)")
