import random as rnd
counter = 0
how_many_rolls = int(input("How many times would you like to roll the dice? : "))
while how_many_rolls >0:

    how_many_rolls -= 1
    guess = input("Roll the dice? (y/n):")

    guess = guess.lower()

    if guess == "y":   
        counter+=1
        print(f"({rnd.randint(1,6)},{rnd.randint(1,6)})")

    elif guess == "n":
        print("Thank you for playing!")
        print(f"You rolled the dice {counter} times.")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

if how_many_rolls == 0:
    print("Thank you for playing!")
    print(f"You rolled the dice {counter} times.")  