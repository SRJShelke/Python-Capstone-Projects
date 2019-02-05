#Find e to the Nth Digit - Just like the previous problem, but with e instead of PI. Enter a number and have the program generate e up to that many decimal places. Keep a limit to how far the program will go.



import math

dec = input("Enter the decimal no. in between 1 to 10 => ")
print "you have entered the number => ",dec

print "Actual value of the e => ",math.e

print round(math.e, dec)