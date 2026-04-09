age = input("Enter your age ")

while not age.isdigit:
    print("Error, please enter a number")
    age = input("Enter a larger number ")
print("Congratulations! You are an adult") 
# year = age + 1
# print(f"On your next birthday, you will be {year}.")

# egg_num = int(input("How many egg cartons do you have? "))
# egg_total = egg_num * 12
# print(f"You have {egg_total} eggs")

# num_of_cookies = int(input("How many cookies do you have? "))
# num_of_people = int(input("How many people are there? "))
# cookies_per_person = num_of_cookies / num_of_people
# print(f"Each person will have {cookies_per_person} cookies")