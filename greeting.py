#Write a function that takes a name and time of day (morning, afternoon, evening) and returns a suitable greeting.
def greeting(name, time):
    if time == "morning":
        print(f"Good Morning {name}")
    elif time == "afternoon":
        print(f"Good Afternoon {name}")
    elif time == 'evening':
        print(f"Good Evening {name}")
    
    else:
        print("Invalid Time")
        
    
        
name = input("Enter your name : ")
time = input("Enter time of the day (morning, afternoon, evening) : ")
greeting(name, time)