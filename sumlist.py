#Write a function that returns the sum of all elements in a list of numbers.

   
def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


# Input: 1 2 3 4 5
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("List:", numbers)
result=sum_of_list(numbers)
print(result)

