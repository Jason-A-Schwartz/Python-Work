# Jason Schwartz
# CINF 308: Programing For Informatics Assignment Nine

# This creates the Data class which stores the DataPoints object which takes 3 values 'UFN','UG', and 'MFN': UFN will collect the Users Favorite Number input, UG will collect the Users Guess input, and MFN will store My Favorite Number
class Data:
    def __init__(DataPoints, UFN, UG, MFN):

        # This assigns passable values to the DataPoints object
        DataPoints.UFN = UFN
        DataPoints.UG = UG
        DataPoints.MFN = MFN

# This creates the Calculations class which uses inheritance to obtain the 'UFN', 'UG', and 'MFN' parameters from the DataPoints object.
class Calculations(Data):

    # These functions have parameters passed from the DataPoints Object (which is from the inherited Data class) in order to return various calculations
    def Add(DataPoints):

        # This takes My Favorite Number and adds it to the User Favorite Number Input and then returns it
        return(DataPoints.MFN + DataPoints.UFN)

    def Sub(DataPoints):

        # This takes My Favorite Number and subtracts it from the User Favorite Number Input and then returns it
        return(DataPoints.MFN - DataPoints.UFN)

    def Mul(DataPoints):

        # This takes My Favorite Number and multiplies it by the User Favorite Number Input and then returns it
        return(DataPoints.MFN * DataPoints.UFN)

    def Div(DataPoints):

        # This takes My Favorite Number and divides it by the User Favorite Number Input and then returns it
        return(DataPoints.MFN / DataPoints.UFN)

    def Mod(DataPoints):

        # This takes My Favorite Number and the User Favorite Number Input and preforms a modulus calculation
        return(DataPoints.MFN % DataPoints.UFN)

# This creates the GCount variable that will be used later in order to track the number of guesses the user needs to get my favorite number right
GCount = 1

# This creates the DataPass variable which goes into the Data class and passes information to the DataPoints object which takes 3 values 'UFN', 'UG', and 'MFN'
DataPass = Data(0, 0, 15)

# This describes to the user what the program will do
print("\nThis program uses classes, objects, inheritance, functions, user input, and loops to ask some questions and preform some calculations.")

# This loop checks if the user input is valid. If it isn't it prints an error message and loops in order to ask again. However, if it is valid, it assigns the user value to a variable and breaks the loop
while True:

    # This runs until an input is made that breaks the loop and doesn't cause an error
    try:

        # This allows the user to input their favorite number which passes it to the DataPoints object's first value 'UFN'
        DataPass.UFN = float(input("\nPlease enter YOUR favorite number: "))

        # This breaks the loop if no error is caught
        break

    # This catches an error if the user did not put in a valid number input and displays a message before restarting the loop
    except ValueError:
        print("\nERROR: Please enter a number!")

# This creates the Answers variable which goes into the Calculations class to get the passed 'UFN', 'UG', and 'MFN' variables (which were inherited from the Data class)
Answers = Calculations(DataPass.UFN,DataPass.UG,DataPass.MFN)

# This loop checks if the user input is valid. If it isn't it prints an error message and loops in order to ask again. However, if it is valid, it goes through the if elif statement until it gets the "correct" answer and breaks the loop
while True:

    # This runs until an input is made that breaks the loop and doesn't cause an error
    try:

        # This allows the user to guess my favorite number and passes it to the DataPoints object's second value 'UG'
        DataPass.UG = float(input("\nPlease guess MY favorite number: "))

        # This if elif branch tests the user input and the object values to see if the user had guess the right number. If they do it displays the final message with the calculations. If they do not get it right it adds to the counter and has them try again with a hint. Also it accounts for being grammatically correct: 1 guess vs 2 guesses
        if DataPass.UG == DataPass.MFN and GCount == 1:
            # This pulls from the Data class's DataPoints object and the Calculations class's functions to display the final message and calculations
            print("\nCongratulations, you guessed it!\n\nNow, MY favorite number '", DataPass.MFN, "' + YOUR favorite number '", DataPass.UFN, "' =", Answers.Add(), "\n\nHowever, MY favorite number '", DataPass.MFN, "' - YOUR favorite number '", DataPass.UFN, "' =", Answers.Sub(), "\n\nAnd, MY favorite number '", DataPass.MFN, "' * YOUR favorite number '", DataPass.UFN, "' =", Answers.Mul(), "\n\nOh wait! MY favorite number '", DataPass.MFN, "' / YOUR favorite number '", DataPass.UFN, "' =", Answers.Div(),  "\n\nAnd finally, MY favorite number '", DataPass.MFN, "' % YOUR favorite number '", DataPass.UFN, "' =", Answers.Mod(), "\n\nIt only took you:", GCount, "guess!\n")
            break
        elif DataPass.UG == DataPass.MFN and GCount != 1:
            # This pulls from the Data class's DataPoints object and the Calculations class's functions to display the final message and calculations but grammatically correct: 1 guess vs 2 guesses
            print("\nCongratulations, you guessed it!\n\nNow, MY favorite number '", DataPass.MFN, "' + YOUR favorite number '", DataPass.UFN, "' =", Answers.Add(), "\n\nHowever, MY favorite number '", DataPass.MFN, "' - YOUR favorite number '", DataPass.UFN, "' =", Answers.Sub(), "\n\nAnd, MY favorite number '", DataPass.MFN, "' * YOUR favorite number '", DataPass.UFN, "' =", Answers.Mul(), "\n\nOh wait! MY favorite number '", DataPass.MFN, "' / YOUR favorite number '", DataPass.UFN, "' =", Answers.Div(),  "\n\nAnd finally, MY favorite number '", DataPass.MFN, "' % YOUR favorite number '", DataPass.UFN, "' =", Answers.Mod(), "\n\nIt only took you:", GCount, "guesses!\n")
            break
        elif DataPass.UG < DataPass.MFN:
            # This adds to the count if they guessed wrong and gives a "smaller" hint
            GCount = GCount + 1
            print("\nYou've guessed too small, try again!")
        elif DataPass.UG > DataPass.MFN:
            # This adds to the count if they guessed wrong and gives a "higher" hint
            GCount = GCount + 1
            print("\nYou've guessed too high, try again!")

    # This catches an error if the user did not put in a valid number input and displays a message before restarting the loop
    except ValueError:
        print("\nERROR: Please enter a number!")