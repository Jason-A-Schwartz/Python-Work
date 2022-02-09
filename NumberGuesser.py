# Jason Schwartz
# CINF 308: Programing For Informatics Assignment Two

# This describes to the user what the program will do
print("\nThis program will: \n\n1) Ask for YOUR favorite number \n2) Then make you guess MY favorite number \n3) And finally it will calculate some numbers based on your input while keeping track of how many guesses you needed")

# This is my favorite number being defined as a variable to be used later
MyFavoriteNumber = float(15)

# This creates the variable that will be added to in order to track the number of guesses the user uses to get my favorite number
GCount = 1

# This loop checks if the user input is valid. If it isn't it prints an error message and loops in order to ask again. However, if it is valid, it assigns the user value to a variable and breaks the loop
while True:

    # This runs until an input is made that breaks the loop and doesn't cause an error
    try:

        # This allows the user to input their favorite number
        YourFavoriteNumber = float(input("\nPlease enter YOUR favorite number: "))

        # This breaks the loop if no error is caught
        break

    # This catches an error if the user did not put in a valid number input and displays a message before restarting the loop
    except ValueError:
        print("\nERROR: Please enter a number!")

# This adds my favorite number and the users favorite number together and assigns it to a variable in order to display it as a sum later
AnswerOne = MyFavoriteNumber + YourFavoriteNumber
AnswerTwo = MyFavoriteNumber - YourFavoriteNumber
AnswerThree = MyFavoriteNumber * YourFavoriteNumber

# This loop checks if the user input is valid. If it isn't it prints an error message and loops in order to ask again. However, if it is valid, it goes through the if elif statement until it gets the "correct" answer and breaks the loop
while True:

    # This runs until an input is made that breaks the loop and doesn't cause an error
    try:

        # This allows the user guess my favorite number
        Guess = float(input("\nPlease guess MY favorite number: "))

        # This if elif branch tests the user input to see if they guess the right number. If they do it displays the final message with the calculations. If they do not get it right it adds to the counter and has them try again with a hint. Also it accounts for being grammatically correct: 1 guess vs 2 guesses
        if Guess == MyFavoriteNumber and GCount == 1:
            print("\nCongratulations, you guessed it!\n\nNow, MY favorite number '", MyFavoriteNumber, "' + YOUR favorite number '", YourFavoriteNumber, "' =", AnswerOne, "\n\nHowever, MY favorite number '", MyFavoriteNumber, "' - YOUR favorite number '", YourFavoriteNumber, "' =", AnswerTwo, "\n\nAnd, MY favorite number '", MyFavoriteNumber, "' * YOUR favorite number '", YourFavoriteNumber, "' =", AnswerThree,"\n\nIt only took you:",GCount,"guess!")
            break
        elif Guess == MyFavoriteNumber and GCount != 1:
            print("\nCongratulations, you guessed it!\n\nNow, MY favorite number '", MyFavoriteNumber, "' + YOUR favorite number '", YourFavoriteNumber, "' =", AnswerOne, "\n\nHowever, MY favorite number '", MyFavoriteNumber,"' - YOUR favorite number '", YourFavoriteNumber, "' =", AnswerTwo, "\n\nAnd, MY favorite number '", MyFavoriteNumber, "' * YOUR favorite number '", YourFavoriteNumber, "' =", AnswerThree, "\n\nIt only took you:", GCount, "guesses!")
            break
        elif Guess < MyFavoriteNumber:
            # This adds to the count if they guessed wrong and gives a "smaller" hint
            GCount = GCount + 1
            print("\nYou've guessed too small, try again!")
        elif Guess > MyFavoriteNumber:
            # This adds to the count if they guessed wrong and gives a "higher" hint
            GCount = GCount + 1
            print("\nYou've guessed too high, try again!")

    # This catches an error if the user did not put in a valid number input and displays a message before restarting the loop
    except ValueError:
        print("\nERROR: Please enter a number!")
