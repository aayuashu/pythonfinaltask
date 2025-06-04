#Create a function that prints a right-angled triangle pattern of * based on the number of rows provided.
def pattern(n):
    for i in range(1, n+1):
        print("*"*i)
        
        
n=int(input("enter no of rows:"))
pattern(n)