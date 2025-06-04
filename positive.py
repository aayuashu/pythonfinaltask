#Write a function that accepts a list of numbers and returns only the positive numbers in a new list.
def positiveNum(listNumbers):
    newList = []
    for element in listNumbers:
        if element > -1:
            newList.append(element)
    return newList



InitialList = map(int, input("Enter list of Numbers : ").split())
positiveNumbersFromInitialList = positiveNum(InitialList)
print("Positive Numbers are : ", end=" ")
for element in positiveNumbersFromInitialList:
    print(element, end=" ")
    
    