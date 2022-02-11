# Jason Schwartz
# CINF 308: Programing For Informatics Assignment Ten

# This imports the random module for the default list
import random

# This creates the default list with 5 random int values between (and including) 1-100. Also, I include it outside the restart loop to allow users to interact with previous changes if they want
DefaultList = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]

# This loops the whole program if the user wants to restart
while True:

    # This explains what the program will do
    print("\nThis program will allow the user to carry out different algorithms on a list based on their inputs")

    # This funtion contains my Search algorithm
    def Search():

        # This describes what the function will do
        print("\nThis is my Search algorithm")

        # This loops until the user inputs a valid list value to search for
        while True:

            # This loops to makes sure that the user input is valid
            while True:

                # This runs until an input is made that breaks the loop and doesn't cause an error
                try:

                    # This displays the current list for the user to see
                    print("\nThis is the current list:\n\n" + str(DefaultList))

                    # This collects user input to manipulate the list
                    UserInput = int(input("\nPlease enter an integer to search for in the list: "))

                    # This breaks the loop if no error is caught
                    break

                # This makes sure the user put in an int and not a str
                except ValueError:
                    print("\nERROR: Please enter an integer!")

            # This creates a boolean value to check if the user input was found in the list or not
            InList = False

            # This loops through the list to see if the user input was in the list or not
            for x in DefaultList:

                # This checks if the user input was in the list and prints/changes the boolean value if it is
                if (UserInput == x):

                    # This prints out the result
                    print("\n" + str(x) + " is in the list!")

                    # This states that the value was indeed in the list
                    InList = True

                    # This breaks the loop
                    break

            # This prints if the user input was not in the list
            if (InList == False):
                print("\nSorry " + str(UserInput) + " is not in the list")

            # This breaks the loop if the user input a valid list value to delete
            if (InList == True):
                break

    # This contains my Sort algorithm
    def Sort():

        # This describes what the function will do
        print("\nThis is my Sort algorithm")

        # This loops to makes sure that the user input is valid
        while True:

            # This runs until an input is made that breaks the loop and doesn't cause an error
            try:

                # This displays the current list for the user to see
                print("\nThis is the current list:\n\n" + str(DefaultList))

                # This collects user input to manipulate the list
                UserInput = int(input("\nPlease enter what type of sort you would like to do:\n\n1. Ascending\n\n2. Descending\n\nEnter your choice here: "))

                # This makes sure that the user input is within the desired range and prints an error if it isn't and then asks again
                while (UserInput != 1 and UserInput != 2):
                    print("\nERROR: Please enter the number associated with the type of sort you want!")
                    UserInput = int(input("\nPlease enter what type of sort you would like to do:\n\n1. Ascending\n\n2. Descending\n\nEnter your choice here: "))
                
                # This checks if the user input 1
                if(UserInput == 1):
                    
                    # This sorts the default list in ascending order
                    DefaultList.sort()

                    # This prints out the results
                    print("\nThis is the list in ascending order:\n\n" + str(DefaultList))

                # This checks if the user input 2
                if(UserInput == 2):

                    # This sorts the default list in descending order
                    DefaultList.sort(reverse = True)

                    # This prints out the results
                    print("\nThis is the list in descending order:\n\n" + str(DefaultList))

                # This breaks the loop if no error is caught
                break

            # This makes sure the user put in an int and not a str
            except ValueError:
                print("\nERROR: Please enter an integer!")

    # This contains my Insert algorithm
    def Insert():

        # This describes what the function will do
        print("\nThis is my Insert algorithm")

        # This loops to makes sure that the user input is valid
        while True:

            # This runs until an input is made that breaks the loop and doesn't cause an error
            try:

                # This displays the current list for the user to see
                print("\nThis is the current list:\n\n" + str(DefaultList))

                # This collects user input to manipulate the list
                UserInput = int(input("\nPlease enter an integer to insert into the list: "))

                # This breaks the loop if no error is caught
                break

            # This makes sure the user put in an int and not a str
            except ValueError:
                print("\nERROR: Please enter an integer!")

        # This loops to makes sure that the user input is valid
        while True:

            # This runs until an input is made that breaks the loop and doesn't cause an error
            try:

                # This displays the current list for the user to see
                print("\nThis is the current list:\n\n" + str(DefaultList))

                # This lets the user know how many values are currently in the list
                print("\nThere are currently " + str(len(DefaultList)) + " values in the list")

                # This collects user input to manipulate the list
                IndexChoice = int(input("\nNow please enter at what value you want to input your number in the list: "))
                
                # This makes sure that the user input is in the valid range and if not it prints an error and asks again (this accounts for lists starting at index 0 by adding one to the length range)
                while(IndexChoice > (len(DefaultList) + 1) or IndexChoice <= 0):

                    print("\nERROR: The value must be within the size of the list")
                    IndexChoice = int(input("\nNow please enter at what value you want to input your number in the list: "))

                # This accounts for lists starting at 0 by subtracting one from the user index choice
                IndexChoice -= 1
                IndexReport = IndexChoice + 1
                
                # This inserts the user input at their index choice in the default list with regards to some corrections accounting for lists starting at 0
                DefaultList.insert(IndexChoice,UserInput)

                # This prints the new list with correct values for the user to understand
                print("\nThis is the new list with your number: " + str(UserInput) + " at value: " + str(IndexReport) + ":" + "\n\n" + str(DefaultList))

                # This breaks the loop if no error is caught
                break
            
            # This makes sure the user put in an int and not a str
            except ValueError:
                print("\nERROR: Please enter an integer!")

    # This contains my Update algorithm
    def Update():

        # This describes what the function will do
        print("\nThis is my Update algorithm")

        # This loops until the user inputs a valid list value to search for
        while True:

            # This loops to makes sure that the user input is valid
            while True:

                # This runs until an input is made that breaks the loop and doesn't cause an error
                try:

                    # This displays the current list for the user to see
                    print("\nThis is the current list:\n\n" + str(DefaultList))

                    # This collects user input to manipulate the list
                    UserInput = int(input("\nPlease enter an integer to update from the list: "))

                    # This breaks the loop if no error is caught
                    break

                # This makes sure the user put in an int and not a str
                except ValueError:
                    print("\nERROR: Please enter an integer!")

            # This creates a boolean value to check if the user input was found in the list or not
            InList = False

            # This loops through the list to see if the user input was in the list or not
            for x in DefaultList:

                # This checks if the user input was in the list and prints/changes the boolean value if it is
                if (UserInput == x):

                    # This loops to makes sure that the user input is valid
                    while True:

                        # This runs until an input is made that breaks the loop and doesn't cause an error
                        try:

                            # This displays the current list for the user to see
                            print("\nThis is the current list:\n\n" + str(DefaultList))

                            # This collects user input to manipulate the list
                            UserUpdateInput = int(input("\nNow, please enter the new integer you want added: "))

                            # This breaks the loop if no error is caught
                            break

                        # This makes sure the user put in an int and not a str
                        except ValueError:
                            print("\nERROR: Please enter an integer!")

                    # This obtains the index of the original non-updated user input value (from the default list) and assigns it to a variable
                    IndexChoice = DefaultList.index(x)

                    # This removes the original non-updated value which was specifed by the user input
                    DefaultList.remove(UserInput)

                    # This inserts the new user input value at the index of the original non-updated value
                    DefaultList.insert(IndexChoice, UserUpdateInput)

                    # This prints out the result
                    print("\nThis is the new list with your updated number:\n\n" + str(DefaultList))

                    # This states that the value was indeed in the list
                    InList = True

                    # This breaks the loop
                    break

            # This prints if the user input was not in the list
            if (InList == False):
                print("\nSorry " + str(UserInput) + " is not in the list")

            # This breaks the loop if the user input a valid list value to delete
            if (InList == True):
                break

    # This contains my Delete algorithm
    def Delete():

        # This describes what the function will do
        print("\nThis is my Delete algorithm")

        # This loops until the user inputs a valid list value to delete
        while True:

            # This loops to makes sure that the user input is valid
            while True:

                # This runs until an input is made that breaks the loop and doesn't cause an error
                try:

                    # This displays the current list for the user to see
                    print("\nThis is the current list:\n\n" + str(DefaultList))
                    
                    # This collects user input to manipulate the list
                    UserInput = int(input("\nPlease enter an integer to delete from the list: "))

                    # This breaks the loop if no error is caught
                    break

                # This makes sure the user put in an int and not a str
                except ValueError:
                    print("\nERROR: Please enter an integer!")

            # This creates a boolean value to check if the user input was found in the list or not
            InList = False

            # This loops through the list to see if the user input was in the list or not
            for x in DefaultList:

                # This checks if the user input was in the list and prints/changes the boolean value if it is
                if (UserInput == x):

                    # This deletes the value specified by the user
                    DefaultList.remove(UserInput)

                    # This prints out the result
                    print("\n" + str(UserInput) + " has been removed from the list!\n\nThis is the new list:\n\n" + str(DefaultList))

                    # This states that the value was indeed in the list
                    InList = True

                    # This breaks the loop
                    break

            # This prints if the user input was not in the list
            if (InList == False):
                print("\nSorry " + str(UserInput) + " is not in the list")

            # This breaks the loop if the user input a valid list value to delete
            if (InList == True):
                break

    # This loops to makes sure that the user input is valid
    while True:
        
        # This runs until an input is made that breaks the loop and doesn't cause an error
        try: 

            # This obtains the users function choice
            FunctionChoice = int(input("\nPlease enter the number associated with the algorithm you want to use: \n\n1. Search\n\n2. Sort\n\n3. Insert\n\n4. Update\n\n5. Delete\n\nEnter your choice here: "))

            # This makes sure the user input is in the valid range and if not prints out an error and asks again
            while (FunctionChoice < 1 or FunctionChoice > 5):

                print("\nERROR: Please enter one of the algorithm numbers!")
                FunctionChoice = int(input("\nPlease enter the number associated with the algorithm you want to use: \n\n1. Search\n\n2. Sort\n\n3. Insert\n\n4. Update\n\n5. Delete\n\nEnter your choice here: "))

            # This breaks the loop if the user followed the instructions
            if(FunctionChoice >= 1 or FunctionChoice <= 5):
                break

        # This makes sure the user put in an int and not a str
        except ValueError:
            print("\nERROR: Please enter one of the algorithm numbers!")

    # This checks the user input to run the corresponding function algorithm
    if (FunctionChoice == 1):

        # This calls the Search function
        Search()

    elif(FunctionChoice == 2):

        # This calls the Sort function
        Sort()

    elif(FunctionChoice == 3):

        # This calls the Insert function
        Insert()

    elif(FunctionChoice == 4):

        # This calls the Update function
        Update()

    elif(FunctionChoice == 5):

        # This calls the Delete function
        Delete()

    # This asks the user if they want to start over and assigns their answer to a variable if it's accepted
    StartOver = input("\nStart over with your current list? (yes/no): ")

    # This checks if the user inputs was a valid response. If not it prints an error and loops in order to ask again
    while StartOver != "yes" and StartOver != "no":

        StartOver = input("\nERROR: Please input: yes or no\n\nStart over with your current list? (yes/no): ")

        # If the user input is valid the loop is broken
        if StartOver == "yes" or StartOver == "no":
            break
    
    # This ends the loop/program if the user input:'no'. However, if they had input yes the main loop/program restarts
    if StartOver == "no":
        break