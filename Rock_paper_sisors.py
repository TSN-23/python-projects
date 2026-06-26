import random as rnd

guess = rnd.choice(["r", "p", "s"])

while True:

    user_input = str(input("Enter your choice (r for rock, p for paper, s for scissors) or type 'exit' to quit: ")).lower()

    if user_input == "exit":
        print("Thank you for playing!")
        break
    elif user_input not in ["r", "p", "s"]:
        print("Invalid input. Please enter 'r', 'p', or 's'.")
        

    elif user_input == guess:
        print(f"The Computer chose {guess}.")
        print(f"You chose {user_input}.")
        print("It's a tie!")
        break
    
    elif (user_input == "r" and guess == "s") or (user_input == "p" and guess == "r") or (user_input == "s" and guess == "p"):
        print(f"The Computer chose {guess}.")
        print(f"You chose {user_input}.")
        print("You win!")
        break
    else:
        print(f"The Computer chose {guess}.")
        print(f"You chose {user_input}.")
        print("You lose!")
        break