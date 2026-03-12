import random

while True:
    input("Please Enter to Roll Dice: ")
    dice = random.randint(1,6)
    print("You Rolled: ",dice)

    again = input("Roll Again? (y/n): ").lower()

    if again!="y":
        print("Thanks for playing !")
        break
