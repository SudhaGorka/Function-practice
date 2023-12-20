#Write a function that takes a character and returns true if it is a vowel, false otherwise .

def check_vowel(char):
    if char=='a' or char=='e' or char=='i' or char=='o' or char=='u' or char=='A' or char=='E' or char=='I' or char=='O' or char=='U':
        return 'True'
    else:
        return 'False'
n= input("Enter a Character: ")

print(check_vowel(n))
