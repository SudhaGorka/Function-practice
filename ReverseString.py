#Write a Python program to reverse a string

def reverse_string(str1):
    rstr1=""
    index=len(str1)
    while index>0:
        rstr1 = rstr1+str1[index-1]
        index=index-1
    return rstr1
print(reverse_string('1234abcd'))





        
