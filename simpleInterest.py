#Write a program to calculate simple interest using a function interest() that can receive Principal amount, time and rate and returns calculated simple interest.
#Do specify default values for rate and time as 10% and 2 years respectively

def interest(principal,time = 2, rate = 0.5):
    SI = (principal*time*rate)/100
    return SI

n = int(input("Enter Principal Amount"))
output=interest(n)
print(" Calculated Simple Interest with 2 year time period  and 10% rate is: ", output)


