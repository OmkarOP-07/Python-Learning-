import random

# Computer randomly chooses: -1 = water, 0 = gun, 1 = snake
computer = random.choice([-1, 0, 1])

yourChoice = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()

# Dictionary to map your input to internal value
youDict = {
    "s": 1,    # Snake
    "w": -1,   # Water
    "g": 0     # Gun
}

# Reverse dictionary to print what computer chose
reverseDict = {
    1: "Snake",
    -1: "Water",
    0: "Gun"
}

# Check for valid input
if yourChoice not in youDict:
    print("Invalid choice. Please enter 's', 'w', or 'g'.")
else:
    you = youDict[yourChoice]

    print(f"You chose: {reverseDict[you]}")
    print(f"Computer chose: {reverseDict[computer]}")

    if computer == you:
        print("Result: It's a draw")
    elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
        print("Result: You win! 🎉")
    else:
        print("Result: You lose! 😢")
