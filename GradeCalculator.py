# Jason Schwartz
# WA5

# This states what the program will do
print("This will calculate and output your final grade based your progress in the course")

# This collects user input and assigns it to a variable
UInputRAT = int(input("Please enter how many RAT's you have completed: "))

# This tests if the input is within the allowed range
while UInputRAT < 1 or UInputRAT > 4:

    # This prints if the user did not put in an acceptable integer in the range
    print("Error, please enter within the range of: 1-4")

    # This asks for user input again
    UInputRAT = int(input("Please enter how many RAT's you have completed: "))

# This declares and establishes the variable for the total RAT score
TotalRATscore = 0 

# This runs for the amount of RAT's the user has completed 
for i in range(UInputRAT):

    # This collects user input and assigns it to a variable
    UInputRATscore = int(input("Input your score for your RAT: "))

    # This tests if the input is within the allowed range
    while UInputRATscore < 0 or UInputRATscore > 5:

        # This prints if the user did not put in an acceptable integer in the range
        print("Error, please enter within the range of: 0-5")

        # This collects user input and assigns it to a variable
        UInputRATscore = int(input("Input your score for your RAT: "))
    
    # This adds the user input score to the total RAT score
    TotalRATscore = TotalRATscore + UInputRATscore

# This calculates your average RAT score score based on user input
AverageRATscore = (TotalRATscore/20)*100

# This prints the current average RAT score based on taken RAT scores
print(("your average RAT score is a: "), (AverageRATscore))

# This takes the RAT input and tests if the WA input is within the allowed ranges
while UInputRAT == 1:

    # This collects user input and assigns it to a variable
    UInputWA = int(input("Please enter how many WA's you have completed: "))

    # This tests if the input is within the allowed range
    while UInputWA != 1 and UInputWA != 2:

        # This prints if the user did not put in an acceptable integer in the range
        print("Error, please enter within the range of 1-2 (based on the amount for RAT's you took): ")

        # This asks for user input again
        UInputWA = int(input("Please enter how many WA's you have completed: "))

        # This tests if the user input passes the accepted range 
        if UInputWA == 1 or UInputWA == 2:

            # This ends the current loop if the range is accepted
            break
    
    # This ends the outer loop if the range is accepted
    break

# This takes the RAT input and tests if the WA input is within the allowed ranges
while UInputRAT == 2:

    # This collects user input and assigns it to a variable
    UInputWA = int(input("Please enter how many WA's you have completed: "))

    # This tests if the input is within the allowed range
    while UInputWA != 3 and UInputWA != 4:

        # This prints if the user did not put in an acceptable integer in the range
        print("Error, please enter within the range of 3-4 (based on the amount for RAT's you took): ")

        # This asks for user input again
        UInputWA = int(input("Please enter how many WA's you have completed: "))

        # This tests if the user input passes the accepted range
        if UInputWA == 3 or UInputWA == 4:

            # This ends the current loop if the range is accepted
            break

    # This ends the outer loop if the range is accepted
    break

# This takes the RAT input and tests if the WA input is within the allowed ranges
while UInputRAT == 3:

    # This collects user input and assigns it to a variable
    UInputWA = int(input("Please enter how many WA's you have completed: "))

    # This tests if the input is within the allowed range
    while UInputWA != 5 and UInputWA != 6:

        # This prints if the user did not put in an acceptable integer in the range
        print("Error, please enter within the range of 5-6 (based on the amount for RAT's you took): ")

        # This asks for user input again
        UInputWA = int(input("Please enter how many WA's you have completed: "))

        # This tests if the user input passes the accepted range
        if UInputWA == 5 or UInputWA == 6:

            # This ends the current loop if the range is accepted
            break

    # This ends the outer loop if the range is accepted
    break

# This takes the RAT input and tests if the WA input is within the allowed ranges
while UInputRAT == 4:

    # This collects user input and assigns it to a variable
    UInputWA = int(input("Please enter how many WA's you have completed: "))

    # This tests if the input is within the allowed range
    while UInputWA != 7:

        # This prints if the user did not put in an acceptable integer in the range
        print("Error, please enter 7 (based on the amount for RAT's you took): ")

        # This asks for user input again
        UInputWA = int(
            input("Please enter how many WA's you have completed: "))

        # This tests if the user input passes the accepted range
        if UInputWA == 7:

            # This ends the current loop if the range is accepted
            break

    # This ends the outer loop if the range is accepted
    break

# This declares and establishes the variable for the total WA score
TotalWAscore = 0

# This runs for the amount of RAT's the user has completed
for i in range(UInputWA):

    # This collects user input and assigns it to a variable
    UInputWAscore = int(input("Input your score for your WA: "))

    # This tests if the input is within the allowed range
    while UInputWAscore < 0 or UInputWAscore > 10:

        # This prints if the user did not put in an acceptable integer in the range
        print("Error, please enter within the range of: 0-10")

        # This collects user input and assigns it to a variable
        UInputWAscore = int(input("Input your score for your WA: "))

    # This adds the user input score to the total RAT score
    TotalWAscore = TotalWAscore + UInputWAscore

# This calculates your average WA score score based on user input
AverageWAscore = (TotalWAscore/70)*100

# This prints the current average RAT score based on taken RAT scores
print(("your average RAT score is a: "), (AverageWAscore))

# This collects user input and assigns it to a variable
UInputPQ = int(input("Please enter how many questions you got right on the Python quiz: "))

# This tests if the input is within the allowed range
while UInputPQ < 0 or UInputPQ > 25:

    # This prints if the user did not put in an acceptable integer in the range
    print("Error, please enter within the range of: 0-25")

    # This asks for user input again
    UInputPQ = int(input("Please enter how many questions you got right on the Python quiz: "))

# This calculates your average Python quiz score based on user input
AveragePQscore = (UInputPQ/25)*100

# This prints the current average Python quiz score based on your input
print(("Your average Python quiz score is a: "), (AveragePQscore))

#This multiplies the averages by their respective weight
CourseAverage = ((AverageRATscore * .2) + (AverageWAscore * .7) + (AveragePQscore * .1))

# This prints the current average course grade based on input scores and calculations
print(("Your average score for the course is a: "), (CourseAverage))
