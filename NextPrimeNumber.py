#Next Prime Number : Have the program find prime numbers until the user chooses to stop asking for the next one.


# m = 'y'

# while (m!='n'):
# 	choice = input("Do you want to find next Prime Number (y/n) ")
# 	if choice == "y":
# 		m = 'y'

		#logic for the prime numbers

def isprime(n):
    if n < 2: return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

primes = (i for i in range(1000) if isprime(i))
choice = 0
while (choice!='n'):
	choice = raw_input("Next?")
	count= 0
	if count < 10 :
		# for p in primes:
		# 	print p
		count = count++
		print count
		count = count+1

    