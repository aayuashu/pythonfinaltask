#Create a function that takes two numbers and an operator (+, -, *, /) and returns the result of the operation.
def calculate(n1,n2, n):
    match n:
        case 1:
            return n1+n2
        case 2:
            return n1-n2
        case 3:
            return n1*n2
        case 4:
            return n1/n2
        case _:
            return "Your input is wrong."
        
a=int(input("enter first number:"))
b=int(input("enter second number:"))
num=int(input("enter 1 for add, 2 for subtract, 3 for multiplication, 4 for division:"))
result=calculate(a,b,num)
print("The result is:", result)