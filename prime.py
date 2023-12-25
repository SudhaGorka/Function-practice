#Write a python function that takes a number as a parameter and checks whether a number is prime or not

def check_prime(num):
    if  num ==1:
        return False
    elif num == 2:        
        return True
    else:
        for i in range(2,num):
            if num%i == 0:
                print(num,"is not a prime number")
            
        print(num,"is a prime number")

n = int(input("Enter a number"))
output = check_prime(n)
        
