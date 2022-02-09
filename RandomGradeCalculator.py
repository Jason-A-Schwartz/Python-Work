# Jason Schwartz
# WA6

# This imports the random module to be used in the first function
import random

# This states what the program will do
print("This will ask users how many students are in the class and then use the random module as well as two functions to output randomly generated (but scaled) grades")

# This is my function for using the random module
def Random_Number():

    # This assigns a random integer (between 0-100 and including 0 and 100) to a variable
    x = random.randint(0, 100)

    # This takes the variable and returns the random integer when the function is called 
    return x

# This is my function for calling the previous function and then determining where it falls on the grade scale
def Random_Calculation():

    # This calls the previous function and assigns its return value to a variable
    y = Random_Number()

    # This tests if the return value is within an A range
    if 100 >= y >= 89:

        # This prints the corresponding message for an A range
        print("Their final score is:", y,"Which is an A")

    # This tests if the return value is within a B range
    elif 88 >= y >= 79:

        # This prints the corresponding message for a B range
        print("Their final score is:", y, "Which is a B")

    # This tests if the return value is within a C range
    elif 78 >= y >= 70:

        # This prints the corresponding message for a C range
        print("Their final score is:", y, "Which is a C")

    # This tests if the return value is within a D range
    elif 69 >= y >= 60:

        # This prints the corresponding message for a D range
        print("Their final score is:", y, "Which is a D")

    # This tests if the return value is within a E range
    elif 59 >= y >= 0:

        # This prints the corresponding message for a E range
        print("Their final score is:", y, "Which is a E")

# This collects user input and assigns it to a variable
UInput = int(input("Please enter how many students are in the class: "))

# This runs for the range that the user input
for i in range(UInput):

    # This calls and runs the second function which also calls and runs the first function
    Random_Calculation()
