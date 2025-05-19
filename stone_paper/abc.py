


## cases  rock - rock = tie
## rock - scissor = rock
## rock - paper = paper
## paper - rock = paper , paper-scissor = scissor , paper - paper = tie


import random

# List of valid items
item_list = ["rock", "paper", "scissors"]

# Get user input
user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

# Validate user input
if user_choice not in item_list:
    print("Invalid choice. Please choose rock, paper, or scissors.")
else:
    # Generate computer choice
    comp_choice = random.choice(item_list)

    print(f"User choice: {user_choice} | Computer choice: {comp_choice}")

    # Determine the winner
    if user_choice == comp_choice:
        print("Both chose the same: It's a tie!")
    elif user_choice == "rock":
        if comp_choice == "scissors":
            print("Rock crushes scissors: You win!")
        else:
            print("Paper covers rock: Computer wins!")
    elif user_choice == "paper":
        if comp_choice == "rock":
            print("Paper covers rock: You win!")
        else:
            print("Scissors cut paper: Computer wins!")
    elif user_choice == "scissors":
        if comp_choice == "paper":
            print("Scissors cut paper: You win!")
        else:
            print("Rock crushes scissors: Computer wins!")
