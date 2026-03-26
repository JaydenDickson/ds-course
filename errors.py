# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program") #Syntax error, added brackets
print("\n") #Syntax error, added brackets. Indentation errors below

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24 years old" #Runtime error, == becomes =.
age = int(age_Str[0:2]) #Runtime error, can't cast that string to an int
print(f"I'm {age} years old.")   #Runtime error, can't add string and ints in this way

    # Variables declaring additional years and printing the total years of age
years_from_now = "3"
total_years = age + int(years_from_now) #Runtime error, can't add strings and ints like this

print("The total number of years:" + f"{total_years}")     #Syntax error, added brackets
#Logic error, wrong variable and type used

# Variable to calculate the total number of months from the given number of years and printing the result
total_months = total_years * 12 #Syntax error, wrong variable used
print(f"In 3 years and 6 months, I'll be {total_months + 6} months old")   #Syntax error, added brackets. Syntax error, can't add strings and ints like this

#HINT, 330 months is the correct answer
