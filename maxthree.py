#Write a function that returns the largest among three given numbers.
def checking(n1,n2,n3):
    if n1>n2 & n1>n3:
        return n1
    elif n2>n1 & n2>n3:
        return n2
    else:
        return n3
a,b,c=map(int,input("enter 3 numbers separated by space:").split())
result=checking(a,b,c)
print("The largest among three is:", result)


