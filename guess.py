import random
import math

guessCount = 0
maxGuesses = 5
guess = int

won = False

bsList = ["YOU IDIOT!", "CAN SOMEBODY CALL THE WAMBULANCE", "YOU'RE WRONG, CRY ME A RIVER!", "AWW, YOU GONNA CRY LIKE A LITTLE BITCH?", "DO BETTER!"]

secretNumber = random.randint(1,20)
print(secretNumber)

while guessCount < maxGuesses and won!=True:

    try:
        guess = int(input("Enter a  number in the range [1, 20] (or 0 to quit): "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue

    # Give the user a clear way to exit the program
    if guess == 0:
        print("CONGRATULATIONSS, YOU MADE IT OUTT! NOW PISS OFF!")
        break

    # Validate the entered value    
    if guess not in range(1, 21):
        print("ARREY, CHOTI BACHHII HO KYAA, READ THE INSTRUCTIONS!!!")
        continue

    # Main Logic   
    if guess != secretNumber:
        guessCount+=1
        print(bsList[random.randint(0,4)])
    else:
        won=True 
        if guessCount == 1:
            print("YOU WONN! BIG DICK ENERGY!")
        elif guessCount == 2:
            print("EHH, WHATEVER, BIG DEAL!")
        else:
            print(f"YOU SEEING THIS SHIT? THIS BITCH ACTUALLY TOOK {guessCount} GUESSES!")


