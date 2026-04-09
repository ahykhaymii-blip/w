print("welcome to CSE101")

name = "Akan"
age = 40

print("name")
print("age")

print(f"Your name is {name}")
print(f"Your age is {age}")

print(f"Hello! {name}, you are {age} years old")


place = input("Where are you from? ")
vacation_place = input("where do you want to go to for vacation? ")

print(f"You are from {place}")
print(f"And you want to go to {vacation_place} for vacation")

color = input("Please type in your favourite color ").lower()
if color == "yellow": 
    print("error")
else:
    print(f"Your favourite color is {color}")

# Working with numbers, and converting numbers to strings

song1 = 250
song2 = 100

playlist = song1 + song2

print(playlist)