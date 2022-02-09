# Jason Schwartz
# CINF 308 Assignment Six

# This will be used for the chance element later on
import random

# This tuple is used for a random value generator later on
BridgeBreak = ("yes","no")

# This makes sure the user level is reset when the program opens up
Level = 0

# These establish the Restart variables even though they wont be assigned/updated until later
RestartOne = ""
RestartTwo = ""
RestartThree = ""
RestartFour = ""
RestartFive = ""

# This establishes the skill tree dictionary
Skills = {
    "lp": "Lock Picker"
}

# This is the start of the instructions loop to give the user some information and the ability to quit if they want
while True:

    # This ends the game if the user chose so on one of the endings
    if(RestartOne == "no"):
        break
    # This ends the game if the user chose so on one of the endings
    if(RestartTwo == "no"):
        break
    # This ends the game if the user chose so on one of the endings
    if(RestartThree == "no"):
        break
    # This ends the game if the user chose so on one of the endings
    if(RestartFour == "no"):
        break
    # This ends the game if the user chose so on one of the endings
    if(RestartFive == "no"):
        break

    # This resets the Restart variables even though it wont be assigned/updated until later
    RestartOne = ""
    RestartTwo = ""
    RestartThree = ""
    RestartFour = ""
    RestartFive = ""

    # This resets the user inventory
    Inventory = []
    
    # This describes the program
    print("\nThis is a text based game with multiple storylines/endings and uses a list, dictionary, and tuple. Also, there is the ability to level up, use a skill, and even a chance element!\n")

    # This tells the player how to play
    print("Please only use 'yes' or 'no' to interact with the game unless instructed otherwise\n")

    # This gives the user the option to continue or not
    UserInputChoice = input("Would you like to play?: ")

    # This makes sure the user input is correct and keeps asking until it is
    while UserInputChoice != "yes" and UserInputChoice != "no":
        print("\nError! Please type 'yes' or 'no'")
        UserInputChoice = input("\nWould you like to play?: ")

    # This quits the program if the user doesnt want to play
    if(UserInputChoice == "no"):
        print("\nOkay! Goodbye :)")
        break

    # This starts the game loop if the player does want to play
    if(UserInputChoice == "yes"):
        print("\nGood luck!\n")

    # This is the actual start of the game loop incase the user wants to restart
    while True:

        # This exits to the outer loop to try and restart the game
        if(RestartThree == "yes"):
            break
        # This exits to the outer loop to try and exit the game
        if(RestartThree == "no"):
            break
        # This exits to the outer loop to try and restart the game
        if(RestartFour == "yes"):
            break
        # This exits to the outer loop to try and exit the game
        if(RestartFour == "no"):
            break
        # This exits to the outer loop to restart the game
        if(RestartFive == "yes"):
            break
        # This exits to the outer loop to try and exit the game
        if(RestartFive == "no"):
            break

        # This exits the game if the user selected to opt out
        if(UserInputChoice == "no"):
            break

        # This takes user input to progress the story
        ChoiceOne = input("Welcome to the castle, would you like to enter?: ")

        # This makes sure the user input is correct and keeps asking until it is
        while ChoiceOne != "yes" and ChoiceOne != "no":
            print("\nError! Please type 'yes' or 'no'")
            ChoiceOne = input("\nWelcome to the castle, would you like to enter?: ")

        # This carries out a branch of the story
        if(ChoiceOne == "yes"):
            print("\nYou enter the castle.")

        # This carries out a branch of the story
        if(ChoiceOne == "no"):
            ChoiceTwo = input("\nYou turn away from the castle. From the outside you start to travel down a long twisted path to try and figure out what to do now.\n\nThankfully you come across a bridge that hangs over a very large cavern. Do you want to try and cross it?: ")

            # This makes sure the user input is correct and keeps asking until it is
            while ChoiceTwo != "yes" and ChoiceTwo != "no":
                print("\nError! Please type 'yes' or 'no'")
                ChoiceTwo = input("\nYou turn away from the castle. From the outside you start to travel down a long twisted path to try and figure out what to do now.\n\nThankfully you come across a bridge that hangs over a very large cavern. Do you want to try and cross it?: ")

             # This checks if the user said no and carries out a branch of the story
            if(ChoiceTwo == "no"):
                print("\nYou decide not to cross it and to head back to the castle and enter it")

            # This checks if the user said yes and then pulls a random value from the tuple and assigns it to a variable
            if(ChoiceTwo == "yes"):
                BridgeChance = random.choice(BridgeBreak)
    
                # This checks the random tuple variable and carries out a branch of the story
                if(BridgeChance == "yes"):
                    RestartOne = input("\nThe bridge broke while you tried to cross and you died. Would you like to try again?: ")

                    # This makes sure the user input is correct and keeps asking until it is
                    while RestartOne != "yes" and RestartOne != "no":
                        print("\nError! Please type 'yes' or 'no'")
                        RestartOne = input("\nThe bridge broke while you tried to cross and you died. Would you like to try again?: ")

                    # This exits the game by breaking out of this while loop (breaks out of the outer loop below)
                    if(RestartOne == "no"):
                        print("\nThank you for playing!\n")
                        break

                    # This restarts the game by breaking out of this while loop (breaks out of the outer loop below)
                    if(RestartOne == "yes"):
                        break

                # This checks the random tuple variable and carries out a branch of the story
                if(BridgeChance == "no"):
                    RestartTwo = input("\nThe bridge didn't break and you made it across. Congrats you escaped! Would you like to try again?: ")

                    # This makes sure the user input is correct and keeps asking until it is
                    while RestartTwo != "yes" and RestartTwo != "no":
                        print("\nError! Please type 'yes' or 'no'")
                        RestartTwo = input("\nThe bridge didn't break and you made it across. Congrats you escaped! Would you like to try again?: ")

                    # This exits the game by breaking out of this while loop (breaks out of the outer loop below)
                    if(RestartTwo == "no"):
                        print("\nThank you for playing!\n")
                        break

                    # This restarts the game by breaking out of this while loop (breaks out of the outer loop below)
                    if(RestartTwo == "yes"):
                        break

        # This carries out a branch of the story
        ChoiceThree = input("\nOnce you enter there are two doors...Enter 'yes' for LEFT and enter 'no' for RIGHT!: ")

        # This makes sure the user input is correct and keeps asking until it is
        while ChoiceThree != "yes" and ChoiceThree != "no":
            print("\nError! Please type 'yes' or 'no'")
            ChoiceThree = input("\nOnce you enter there are two doors...Enter 'yes' for LEFT and enter 'no' for RIGHT!: ")

        # This carries out a branch of the story
        if(ChoiceThree == "yes"):
            LevelInput = input("\nYou went LEFT. From here, you see a lock pick on the floor will you add it to your inventory?: ")

            # This makes sure the user input is correct and keeps asking until it is
            while LevelInput != "yes" and LevelInput != "no":
                print("\nError! Please type 'yes' or 'no'")
                LevelInput = input( "\nYou went LEFT. From here, you see a lock pick on the floor will you add it to your inventory?: ")

            # This checks the user input and then adds to current level and appends the lock pick to the list all while progessing a branch of the story
            if(LevelInput == "yes"):
                Level = Level + 1
                Inventory.append("Lock Pick")
                ChoiceFour = str(input("\nCongrats you leveled up! You're now level: " + str(Level) + ". You have also earned the Lock Picker skill! Please enter the skill key to unlock it ('lp'): "))

                # This makes sure the user input is correct and keeps asking until it is
                while (Skills.get(ChoiceFour, "Not a valid key") == "Not a valid key"):
                    print("\nError! Please enter the correct skill key")
                    ChoiceFour = str(input("\nCongrats you leveled up! You're now level: " + str(Level) + ".You have also earned the Lock Picker skill! enter the skill key to unlock it ('lp'): "))
                
                # This makes sure the user input is correct in terms of the dictionary key and progresses the branch of the story
                if (Skills.get(ChoiceFour, "Not a valid key") != "Not a valid key"):
                    ChoiceFive = input("\nAwesome! You have unlocked the: " + str(Skills.get(ChoiceFour)) + " Skill. You now come across a locked door. Would you like to unlock it with your new skill?: ")

                    # This makes sure the user input is correct and keeps asking until it is
                    while ChoiceFive != "yes" and ChoiceFive != "no":
                        print("\nError! Please type 'yes' or 'no'")
                        ChoiceFive = input("\nAwesome! You have unlocked the: " + str(Skills.get(ChoiceFour)) + " Skill. You now come across a locked door. Would you like to unlock it with your new skill?: ")

                    # This carries out a branch of the story
                    if(ChoiceFive == "yes"):
                        RestartThree = input("\nCongrats you unlocked the door and escaped! Would you like to play again?: ")

                        # This makes sure the user input is correct and keeps asking until it is
                        while RestartThree != "yes" and RestartThree != "no":
                            print("\nError! Please type 'yes' or 'no'")
                            RestartThree = input("\nCongrats you unlocked the door and escaped! Would you like to play again?: ")

                        # This exits the game by breaking out of this while loop (breaks out of the outer loop above)
                        if(RestartThree == "no"):
                            print("\nThank you for playing!\n")
                            break

                        # This restarts the game by breaking out of this while loop (breaks out of the outer loop above)
                        if(RestartThree == "yes"):
                            break

                    # This carries out a branch of the story
                    if(ChoiceFive == "no"):
                        RestartFour = input("\nYou choose to not unlock the door and the dragon eats you alive. Would you like to play again?: ")

                        # This makes sure the user input is correct and keeps asking until it is
                        while RestartFour != "yes" and RestartFour != "no":
                            print("\nError! Please type 'yes' or 'no'")
                            RestartFour = input("\n\nYou choose to not unlock the door and the dragon eats you alive. Would you like to play again?: ")

                        # This exits the game by breaking out of this while loop (breaks out of the outer loop above)
                        if(RestartFour == "no"):
                            print("\nThank you for playing!\n")
                            break

                        # This restarts the game by breaking out of this while loop (breaks out of the outer loop above)
                        if(RestartFour == "yes"):
                            break

            # This carries out a branch of the story
            if(LevelInput == "no"):
                print("\nYou don't pick up the lock pick and you keep going forward.\n\nHowever, you realize that there is a locked door and when you go back the lock pick is gone so you head down the RIGHT instead.")

        # This carries out a branch of the story
        if(ChoiceThree == "no"):
            print("\nYou went RIGHT")
        
        # This carries out a branch of the story
        RestartFive = input("\nYou head down the RIGHT path and fall into a pit and die. Would you like to play again?: ")

        # This makes sure the user input is correct and keeps asking until it is
        while RestartFive != "yes" and RestartFive != "no":
            print("\nError! Please type 'yes' or 'no'")
            RestartFive = input("\nYou head down the RIGHT path and fall into a pit and die. Would you like to play again?: ")

        # This exits the game by breaking out of this while loop (breaks out of the outer loop above)
        if(RestartFive == "no"):
            print("\nThank you for playing!\n")
            break

        # This restarts the game by breaking out of this while loop (breaks out of the outer loop above)
        if(RestartFive == "yes"):
            break