import random

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
        print(f"\n{bsList[random.randint(0,4)]}\n")

    else:
        won=True 
        if guessCount == 1:
            print("\nYOU WONN! BIG DICK ENERGY!\n")
        elif guessCount == 2:
            print("\nEHH, WHATEVER, BIG DEAL!\n")
        else:
            print(f"\nYOU SEEING THIS SHIT? THIS BITCH ACTUALLY TOOK {guessCount} GUESSES!\n")

if won==True:
    print("YAYYYY YOU WON!!")
else:
    print("YOU'RE PATHETICCC!")