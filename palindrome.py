#Write a function that checks whether a given string is a palindrome.
def palindromecheck(str):
    reverse=str[::-1]
    return str == reverse

str=input("enter a string:")
print(f"{str} is Palindrome" if palindromecheck(str)==True else f"{str} is Not Palindrome")