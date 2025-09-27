flag = True

while flag:
    userInput = int(input("Enter a number in the range [1, 20] or 0 to exit: "))

    # Give the user a clear way to exit the program
    if userInput == 0:
        print("CONGRATULATIONSS, YOU MADE IT OUTT! NOW PISS OFF!")
        break

    # Validate the entered value    
    if userInput not in range(1, 21):
        print("ARREY, CHOTI BACHHII HO KYAA, READ THE INSTRUCTIONS!!!")