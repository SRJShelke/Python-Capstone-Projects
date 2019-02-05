#Find PI to the Nth Digit - Enter a number and have the program generate PI up to that many decimal places. Keep a limit to how far the program will go.


import math

dec = input("Enter the decimal no. in between 1 to 10")
print "you have entered the number => ",dec

print "Actual value of the PI => ",math.pi

print round(math.pi, dec)