#Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.

num = input("Enter the number => ")

# change this value for a different result
num = 10

# uncomment to take input from the user
#num = int(input("How many terms? "))

# first two terms
n1 = 0
n2 = 1
count = 0

# check if the number of terms is valid
if num <= 0:
   print("Please enter a positive integer")
elif num == 1:
   print("Fibonacci sequence upto",num,":")
   print(n1)
else:
   print("Fibonacci sequence upto",num,":")
   while count < num:
       print n1,","
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1