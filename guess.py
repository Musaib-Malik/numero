# Required libraries
import random
from rich.console import Console
from rich.text import Text

# Initialize the rich console
console = Console()

# Required variables
guessCount = 0
maxGuesses = 5
guess = 0
previousDistance = 0
won = False
secretNumber = random.randint(1,20)

# Use a distinct style for the debug message
console.print(f"Secret Number (for testing): {secretNumber}", style="dim yellow")

# Design the Starting
startText = Text("\n                  ------------------ START ------------------")
startText.stylize("bold magenta")
console.print(startText)

# Welcome Message - Use a calm color for instructions
console.print("\nWell, Hello there. This is a fun guessing game.", style="cyan")
console.print(f"You've got {maxGuesses} guesses to correctly guess the secret number I'm thinking of which is between 1 and 20.", style="cyan")

# Display the mode to quit
console.print("During any guess you can enter the number 0 and the game will quit. Hope you have a fun time!\n", style="cyan")


while guessCount < maxGuesses and not won:

    try:
        # Use a different style for the input prompt
        guess_str = console.input("[bold]Enter a number in the range [1, 20] (or 0 to quit): [/bold]")
        guess = int(guess_str)
    except ValueError:
        # Use a strong, clear color for errors
        console.print("Invalid input. Please enter an integer.", style="bold red")
        continue

    # Give the user a clear way to exit the program
    if guess == 0:
        console.print("Piss off!", style="bold yellow")
        break

    # Validate the entered value    
    if guess not in range(1, 21):
        console.print("Please enter a number in the mentioned range", style="bold red")
        continue

    if guess == secretNumber:
        won=True 
        guessCount+=1
        # Use bright, celebratory colors and styles for winning
        if guessCount == 1:
            console.print("\nYOU WONN! BIG DICK ENERGY! :rocket:", style="bold bright_green on black")
        elif guessCount == 2:
            console.print("\nEHH, WHATEVER, BIG DEAL!", style="bold green")
        else:
            console.print(f"\nYOU SEEING THIS SHIT? THIS BITCH ACTUALLY TOOK {guessCount} GUESSES!", style="bold green")
            console.print("but anyways you won, Yoo-Hoo!", style="green")
   
    elif guess != secretNumber and guessCount>=1:
        newDistance = abs(secretNumber - guess)
        
        # Use intuitive colors for feedback
        if newDistance < previousDistance:
            console.print("Warmer", style="green")
        elif newDistance == previousDistance:
            console.print("Same", style="yellow")
        else:
            console.print("Colder", style="blue")

    else: # This block is for the first guess
        console.print("Nope! Try again.", style="italic")
        
    previousDistance = abs(secretNumber - guess)
    guessCount += 1

if not won:
    # Use a strong color for the loss message
    console.print(f"\nYOU'RE PATHETICCC! You lost such a simple game. The number was {secretNumber}", style="bold bright_red")