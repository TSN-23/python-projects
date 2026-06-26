import random as rnd
secret_number = rnd.randint(1,100)

while True:

    guess = input("Guess a number between 1 and 100 (or type 'exit' to quit): ")
    
    if guess.lower()=="exit":
        print("Thank you for playing!")
        break
    elif type(int(guess)) is int:
        guess = int(guess)
        if guess == secret_number:
            print("Congratulations! You guessed the correct number!")
            break
        elif guess <secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    else:
        print("Invalid input. Please enter a number between 1 and 100.")



