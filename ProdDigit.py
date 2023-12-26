#write a function proddigit() that inputs a number and returns the product of digits of that number.

def Prod_digit(num):
    prod=1
    while(num!=0):   
        digit = num%10
        prod= prod*digit
        num=num//10
    return prod
n=int(input("Enter a two digit number you want product of: "))

print(Prod_digit(n))
    
        
