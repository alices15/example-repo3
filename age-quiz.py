# pseudocode
# 1. ask user to input age
# 2. store as variable "age"
# 3. if:
#   age > 100 display "Sorry, you are dead."
#   age >= 40 display "You're over the hill"
#   age >= 65 display "Enjoy your retirement!"
#   age < 13 display "You qualify for the kiddie discount."
#   age = 21 display "Congrats on your 21st!"
#   else display "Age is but a number"

age = int(input("What is your age?: ")) # asks user for age, converts to an integer for the following if - elif - else functions to work

# checks the age and displays a message based on the age of the person
# note order is important, starts with largest number then decreases, as code is read line by line
if age == 21:
    message = "Congrats on your 21st!"

elif age > 100:
    message = "Sorry, you are dead."

elif age >= 65:
    message = "Enjoy your retirement!"
    
elif age >= 40:
    message = "You're over the hill."

elif age < 13:
    message = "You qualify for the kiddie discount."

else:
    message = "Age is but a number."

print(message)