# Are you eligibel to vot or not:::

# age = int(input("Enter your age: "))

# if age < 18:
#     print("You are not eligible to vote")
# else:
#     citizenship = input("Are you a citizen of Nepal? ")

#     if age >= 18 and citizenship == "Yes":
#         print("You are eligible to vote")
#     else:
#         print("You are not eligible to vote")

# Age and membership + Discount contidion

# age = int(input("Enter your age: "))
# if age >= 70:
#     mmbership = input("Do you have membership: ")
#     if mmbership == "yes":
#         print("You got 30 percentag disount")
#     else:
#         print("You got 20 percentag discount")
# else:
#     print("you dont get any discount")  

# Infinit loop:

# break statnmnt
# count =1 
# while count <10:
#     if count ==3:
#         break
#     print(f"count is {count}")
#     count = +1
# print("Loop ended")

# i = 0
# while i < 5:
#     i += 1
#     if i ==3:
#         continue
# print(i)


# pass Statnment

# count = 0

# while count < 4:
#     count += 1

#     if count == 2:
#         pass
#     else:
#         print(f"Processing number: {count}")


# Number ge=uesssing game : 
"""
-create a program where:
a sectet number is store inside the program.
user keeps entering number
if the number matches, print:
"correct Guess!"
use break to stop the loop. 
if wrong, print:
"Try Again"
"""
num = 89
while True:
    guess_number = int(input("Enter the correct number "))
    if guess_number == num:
        print("Correct guess!")
        break
    else: 
        print("Try again")

