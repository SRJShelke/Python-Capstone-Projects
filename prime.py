'''Next Prime Number - Have the program find prime numbers until the user chooses to stop asking for the next one.'''

def isPrime(n):
    if n < 2: return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def genPrime(currentNumber):
    if isPrime(currentNumber):
        return currentNumber
    

def main():  
    decision = input('Would you like to continue to generate the next prime? (YES/NO) ')
    currentNumber = 2
    while True:

        if decision.lower() == 'yes':
            currentPrime = genPrime(currentNumber)
            if currentPrime:
                print(currentPrime)
                decision = input('Would you like to continue to generate the next prime? (YES/NO) ')
            else :
                currentNumber = currentNumber+1
                continue

        elif decision.lower()=='no' :
            break    
        else:
            decision = input('Please enter valid choice from (YES or No) ? ')

         
        currentNumber = currentNumber + 1


   

if __name__ == '__main__':
    main()


	
	
