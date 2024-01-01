#write a program that inputs a number and print the multiplication table of that number:

def multi_num(num):
    for i in range(1,11):
        print(num, 'x', i, '=',num*i)

n=int(input("Enter a number you want a multiplication table of: "))
multi_num(n)
        
        
