#write a python program to check whether a number fall in range:

def check_range(num):
    if num in range(0,100):
        print( num,"is in range")
    else:
        print(num,"is not in range")

n = int(input("Enter a number which you want to check in range"))
check_range(n)

