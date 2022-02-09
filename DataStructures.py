# Jason Schwartz
# CINF 308: Programing For Informatics Assignment Five

# This establishes a new list
UserNames = ["Jason","Will", "Dan"]
# This establishes a new dictionary with 3 different formats of key inputs for the 12 months of the year
UserMonths = {

    "jan": "January",
    "feb": "February",
    "mar": "March",
    "apr" : "April",
    "may" : "May",
    "jun" : "June",
    "jul" : "July",
    "aug" : "August",
    "sep" : "September",
    "oct" : "October",
    "nov" : "November",
    "dec" : "December",

    "Jan" : "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",

    "JAN": "January",
    "FEB": "February",
    "MAR": "March",
    "APR": "April",
    "MAY": "May",
    "JUN": "June",
    "JUL": "July",
    "AUG": "August",
    "SEP": "September",
    "OCT": "October",
    "NOV": "November",
    "DEC": "December"
}
# This is an examples of atuple which will be used later
EyeColors = ("Brown", "Blue", "Green")

# This explains what the program will do
print("\nHello, this program is a survey that will collect some information about you and then use data structures to store, add, or print it back to you")

# This asks the user to input their name
UserInputName = input("\nPlease enter your name to add it to the list" + "\n\nCurrent list: " + str(UserNames)+ "\n\nEnter your name here: ")
# This catches if the user puts in a int instead of a str and asks them to try again until they get it right
while(UserInputName.isdigit()):
    print("\nError!")
    UserInputName = input("\nPlease enter your NAME to add it to the list" + "\n\nCurrent list: " + str(UserNames) + "\n\nEnter your NAME here: ")
# This appends the user's input to the list
UserNames.append(UserInputName)

# This asks the user to input the month they were born in while using a tuple to show examples
UserinputMonth = input("\nPlease enter the first three letters of the month you were born in" + "\n\nExamples: 'jan', 'Jan', 'JAN'...\n\nEnter the first three letters of your month here: ")
# This catches if the user didn't put in a valid month and asks them to try again until they get it right
while (UserMonths.get(UserinputMonth, "Not a valid key") == "Not a valid key"):
    print("\nError!")
    UserinputMonth = input("\nPlease enter the FIRST THREE letters of the month you were born in" + "\n\nExamples: 'jan', 'Jan', 'JAN'...\n\nEnter the FIRST THREE letters of your month here: ")
    # This breaks the loop when the user puts in the correct format
    if (UserMonths.get(UserinputMonth, "Not a valid key") != "Not a valid key"):
        break

# This asks the user to input their eye color based off the tuple values
UserInputEyeColor = input("\nPlease select the number that is closest to your eye color" + "\n\nChoices:\n" + "\n 1. " + str(EyeColors[0]) + "\n" + "\n 2. " + str(EyeColors[1]) + "\n" + "\n 3. " + str(EyeColors[2]) + "\n" + "\nEnter your number choice here: ")
# This makes sure that the user input is one of the tuple values and has them try again until they get it right
while (UserInputEyeColor != "1" and UserInputEyeColor != "2" and UserInputEyeColor != "3"):
        print("\nError!")
        UserInputEyeColor = input("\nPlease select the NUMBER that is CLOSEST to your eye color" + "\n\nChoices:\n" + "\n 1. " + str(EyeColors[0]) + "\n" + "\n 2. " + str(EyeColors[1]) + "\n" + "\n 3. " + str(EyeColors[2]) + "\n" + "\nEnter your NUMBER choice here: ")

# This checks the user input and assigns it to the corresponding tuple value
if (UserInputEyeColor == "1"):
    UserInputEyeColor = EyeColors[0]
elif(UserInputEyeColor == "2"):
    UserInputEyeColor = EyeColors[1]
elif(UserInputEyeColor == "3"):
    UserInputEyeColor = EyeColors[2]

# These output the final messages with all the values input/stored
print("\nCalculating...")
print("\nRESULTS:")
print("\nNew list with your name added: " + str(UserNames) + "\n" + "\nYour full birth month from the dictionary key: " + str(UserMonths.get(UserinputMonth)) + "\n" + "\nThe eye color you chose from the tuple: " + str(UserInputEyeColor) + "\n")
