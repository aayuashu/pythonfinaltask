#Write a function to compute the factorial of a given number using a loop.
def fact(n):
   if n==0:
       return 1
   else:
       return n*fact(n-1)

num=int(input("enter a number for factorial:"))
answer=fact(num)
print("The factorial is:", answer)
    