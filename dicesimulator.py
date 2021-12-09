import random

TOTAL_SIDES = 6


def roll_dice():
    die1 = random.randint(1,TOTAL_SIDES)
    die2 = random.randint(1, TOTAL_SIDES)

    print("You got " + str(die1) + " in the first dice")
    print("You got " + str(die2) + " in the second dice")

    total = die1 + die2

    print("and so your total are " + str(total))

roll_dice()



