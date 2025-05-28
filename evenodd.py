#Write a function that takes a number as input and returns whether it is even or odd.

def evenodd(num):
    if num%2 ==0:
        return 1
    else:
        return 0
    
#take input
number=int(input("Enter a number:"))
result=evenodd(number)
if result ==1:
    print("It is even number.")
else:
    print("It is odd number.")

'''Enter a number:4
It is even number.

Enter a number:5
It is odd number.'''
