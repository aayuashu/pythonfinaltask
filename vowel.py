#Create a function that counts and returns the number of vowels in a given string.

def counting(sentence):
    vowels ="aeiouAEIOU"
    count =0
    for line in sentence:
        for char in line:
            if char in vowels:
                count+=1
    
    return count
    

user=input("Enter a string:")
result=counting(user)
print("The number of vowels is:", result)

