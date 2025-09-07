from random import randint

# Roll a dice and output a formatted string with the number
sides = int(input("How many sides does the dice have? "))

def roll_dice(sides):
    return randint(1, sides)

number = roll_dice(sides)

print(f"The dice reads: {number}")