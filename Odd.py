#Write a program with a function chkOdd() that takes one argument(a positive integer) and reports if the argument is odd or not.

def checkOdd(num):
    if num%2==0:
        print(num,"is not odd")
    else:
        print(num,"is Odd")
n=int(input("Enter a positive number"))
output=checkOdd(n)

    
