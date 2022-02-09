# Jason Schwartz
# CINF 308: Programing For Informatics Assignment Eight

# This creates the UserInput class which stores the UserAnswer object which takes 2 values 'UFN' and 'UG': UFN will collect the Users Favorite Number input and UG will collect the Users Guess input
class UserInput:
    def __init__(UserAnswer, UFN, UG):

        # This assigns passable values to the UserAnswer object
        UserAnswer.UFN = UFN
        UserAnswer.UG = UG

# This creates the Calculations class which stores the Data object which takes 2 values 'UFN' and 'MFN': UFN will be set to the User Favorite Number input and MFN is My Favorite Number
class Calculations:
    def __init__(Data, UFN, MFN):

        # This assigns passable values to the Data object
        Data.UFN = UFN
        Data.MFN = MFN

    # These are functions that will be used to calculate and return numbers later on
    def Add(Data):

        # This takes My Favorite Number and adds it to the User Favorite Number Input and then returns it
        return(Data.MFN + Data.UFN)

    def Sub(Data):

        # This takes My Favorite Number and subtracts it to the User Favorite Number Input and then returns it
        return(Data.MFN - Data.UFN)

    def Mul(Data):

        # This takes My Favorite Number and multiplies it to the User Favorite Number Input and then returns it
        return(Data.MFN * Data.UFN)

# This creates the GCount variable that will be used later in order to track the number of guesses the user needs to get my favorite number right
GCount = 1

# This creates the UserResponse variable which goes into the UserInput class and passes information to the UserAnswer Object which takes 2 values 'UFN' and 'MFN'
UserResponse = UserInput(0,0)

# This describes to the user what the program will do
print("\nThis program uses objects and user input to obtain your favorite number and then lets you guess mine.\n\nAlso it will use functions to return some calculations based off your/my values")

# This loop checks if the user input is valid. If it isn't it prints an error message and loops in order to ask again. However, if it is valid, it assigns the user value to a variable and breaks the loop
while True:

    # This runs until an input is made that breaks the loop and doesn't cause an error
    try:

        # This allows the user to input their favorite number which passes it to the UserAnswer object's first value 'UFN'
        UserResponse.UFN = float(input("\nPlease enter YOUR favorite number: "))

        # This breaks the loop if no error is caught
        break

    # This catches an error if the user did not put in a valid number input and displays a message before restarting the loop
    except ValueError:
        print("\nERROR: Please enter a number!")

# This creates the DataPoints variable which goes into the Calculations class and passes information to the Data Object's 'UFN' and 'MFN' values
DataPoints = Calculations(UserResponse.UFN, float(15))

# This loop checks if the user input is valid. If it isn't it prints an error message and loops in order to ask again. However, if it is valid, it goes through the if elif statement until it gets the "correct" answer and breaks the loop
while True:

    # This runs until an input is made that breaks the loop and doesn't cause an error
    try:

        # This allows the user to guess my favorite number and passes it to the UserAnswer object's second value 'UG'
        UserResponse.UG = float(input("\nPlease guess MY favorite number: "))

        # This if elif branch tests the user input/object values to see if the user had guess the right number. If they do it displays the final message with the calculations. If they do not get it right it adds to the counter and has them try again with a hint. Also it accounts for being grammatically correct: 1 guess vs 2 guesses
        if UserResponse.UG == DataPoints.MFN and GCount == 1:

            # This pulls from the objects values and the Calculations class functions to display the final message and calculations
            print("\nCongratulations, you guessed it!\n\nNow, MY favorite number '", DataPoints.MFN, "' + YOUR favorite number '", UserResponse.UFN, "' =", DataPoints.Add(), "\n\nHowever, MY favorite number '", DataPoints.MFN,
                  "' - YOUR favorite number '", UserResponse.UFN, "' =", DataPoints.Sub(), "\n\nAnd, MY favorite number '", DataPoints.MFN, "' * YOUR favorite number '", UserResponse.UFN, "' =", DataPoints.Mul(), "\n\nIt only took you:", GCount, "guess!")
            break
        elif UserResponse.UG == DataPoints.MFN and GCount != 1:

            # This pulls from the objects values and the Calculations class functions to display the final message and calculations
            print("\nCongratulations, you guessed it!\n\nNow, MY favorite number '", DataPoints.MFN, "' + YOUR favorite number '", UserResponse.UFN, "' =", DataPoints.Add(), "\n\nHowever, MY favorite number '", DataPoints.MFN,
                  "' - YOUR favorite number '", UserResponse.UFN, "' =", DataPoints.Sub(), "\n\nAnd, MY favorite number '", DataPoints.MFN, "' * YOUR favorite number '", UserResponse.UFN, "' =", DataPoints.Mul(), "\n\nIt only took you:", GCount, "guesses!")
            break
        elif UserResponse.UG < DataPoints.MFN:
            # This adds to the count if they guessed wrong and gives a "smaller" hint
            GCount = GCount + 1
            print("\nYou've guessed too small, try again!")
        elif UserResponse.UG > DataPoints.MFN:
            # This adds to the count if they guessed wrong and gives a "higher" hint
            GCount = GCount + 1
            print("\nYou've guessed too high, try again!")

    # This catches an error if the user did not put in a valid number input and displays a message before restarting the loop
    except ValueError:
        print("\nERROR: Please enter a number!")