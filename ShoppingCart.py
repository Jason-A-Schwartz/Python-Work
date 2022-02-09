# Jason Schwartz
# CINF 308 Asssignment Four

# These declare values so they can be tested at the begining of the first while loop (even though they wont hold anything until later on)
UserInputRestartFull = 0
UserInputRestart = ""

# This is needed to contain the whole program and restart it if the user chooses to do so later on
while True:

    # This quits the program if the user has a full cart and they choose to quit
    if(UserInputRestartFull == 2):
        break
    # This quits the program if the user doesn't want to make any more changes and they choose to quit
    if (UserInputRestart == "no"):
        break

    # This resets the value so the loop doesn't continue forever if the user chose to restart the program
    UserInputRestartFull = 0

    # This creates the empty cart list
    MyCart = []

    # This creates the website list with shoe brands
    WebsiteList = ["nike","vans","adidas"]

    # This states what the program will do
    print("\nThis program will simulate a website experience where you can add and remove items to your cart and or restart/quit")

    # This contains the part of the program that allows the user to come back to the top of the program when they want to add/remove items from the lists
    while True:

        # This is for when the user wants to quit the program with a full cart and is needed to reach the outer while loop
        if(UserInputRestartFull == 2):
            break

        # This is for when the user wants to quit the program with no more changes and is needed to reach the outer while loop
        elif(UserInputRestartFull == 1):
            break

        # This prints the current shoe brand list based on added/removed items
        print("\nCurrent shoe brands for sale:\n\n" + str(WebsiteList))

        # This allows the user to try and add an item to their cart
        CartInput = input("\nWhat would you like to add to your cart?\n\nPlease enter the brand name exactly: ")

        # This makes sure that the user isn't trying to add an item already in the cart
        while(WebsiteList.count(CartInput) == 0):
            print("\nError! Please enter a valid brand name")
            print("\nCurrent shoe brands for sale:\n\n" + str(WebsiteList))
            CartInput = input("\nWhat would you like to add to your cart?\n\nPlease enter the brand name exactly: ")

        # This makes sure that the user is putting in a valid item and asks them to try again until they get it right
        while(CartInput != "nike" and CartInput != "vans" and CartInput != "adidas"):

            print("\nError! Please enter a valid brand name")
            print("\nCurrent shoe brands for sale:\n\n" + str(WebsiteList))
            CartInput = input("\nWhat would you like to add to your cart?\n\nPlease enter the brand name exactly: ")

        # This actually removes the user input item from the website list
        WebsiteList.remove(CartInput)

        # This actually adds the user input item to the cart list
        MyCart.append(CartInput)

        # This displays the users current cart
        print("\nYour current cart: \n\n" +str(MyCart))

        # This checks if the user has a full cart
        if(MyCart.count("nike") + MyCart.count("vans") + MyCart.count("adidas") == 3):

            print("\nYour cart is full!")

            # This asks the user with a full cart to restart the program, or quit and keeps trying until they input a correct format
            while True:
                try:
                    UserInputRestartFull = int(input("\nYour cart is full and you checked out! Now, would you like to:\n\n1. Restart\n\n2. Quit\n\nPlease enter the number you want to do: "))
                    break
                # This catches if the user puts in a str instead of a int
                except ValueError:
                    print("\nError! Please enter a valid NUMBER")

            # This makes sure the user input is in the valid range and if not keeps asking until they input a correct format
            while(UserInputRestartFull < 1 or UserInputRestartFull > 2):
                print("\nError! Please enter a valid NUMBER")
                UserInputRestartFull = int(input("\nWould you like to:\n\n1. Restart\n\n2. Quit\n\nPlease enter the number you want to do: "))
            
        # This quits the program if the user has a full cart and wants to quit (this goes to the outer while loop) to break again
        if(UserInputRestartFull == 2):
            print("\nThank you for shopping!")
            break

        # This restarts the program if the user has a full cart and wants to try again
        elif(UserInputRestartFull == 1):
            break

        # This allows the user to make changes to their cart or quit
        UserInputRestart = input("\nWould you like to make any changes (yes/no)?: ")

        # This makes sure the user input is correct and keeps asking until it is
        while UserInputRestart != "yes" and UserInputRestart != "no":
            print("\nError! Please type 'yes' or 'no'")
            UserInputRestart = input("\nWould you like to make any changes (yes/no)?: ")

        # This quits the program if the user doesnt want to make any more changes (this goes to the outer while loop) to break again
        if (UserInputRestart == "no"):
            print("\nYou checked out with your current cart!")
            break

        # This asks the user if they want to add or remove from their cart and keeps asking until they input a correct format
        while True:
            try:
                UserInputChoice = int(input("\nWould you like to:\n\n1. Add more to your list\n\n2. Remove an item from your list\n\nPlease enter the number you want to do: "))
                break

            # This catches if the user puts in a str instead of an int
            except ValueError:
                print("\nError! Please enter a valid NUMBER")

        # This checks if the user input is in a correct range and keeps asking until it is
        while(UserInputChoice < 1 or UserInputChoice > 2):
            print("\nError! Please enter a valid NUMBER")
            UserInputChoice = int(input("\nWould you like to:\n\n1. Add more to your list\n\n2. Remove an item from your list\n\nPlease enter the number you want to do: "))
            
        # This means the user wants to remove an item and shows them their cart before asking what they want to remove
        if(UserInputChoice == 2):
            print("\nYour cart:\n\n" + str(MyCart))
            CartRemoveInput = input("\nWhat would you like to remove from your cart?\n\nPlease enter the brand name exactly: ")
            
            # This checks to make sure the user input is correct and keeps asking until it is
            while(CartRemoveInput != "nike" and CartRemoveInput != "vans" and CartRemoveInput != "adidas"):

                print("\nError! Please enter a valid brand name")
                print("\nYour cart:\n\n" + str(MyCart))
                CartRemoveInput = input("\nWhat would you like to remove from your cart?\n\nPlease enter the brand name exactly: ")

            # This removes the item the user input from the cart
            MyCart.remove(CartRemoveInput)

            # This adds the item the user removed back to the website list and then loops back to the top with the new list values
            WebsiteList.append(CartRemoveInput)