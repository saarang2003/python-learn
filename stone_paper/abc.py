


## cases  rock - rock = tie
## rock - scissor = rock
## rock - paper = paper
## paper - rock = paper , paper-scissor = scissor , paper - paper = tie

import random
item_list =["rock" , "paper", "scissor"]

user_choice = input("enter your choice  = ")
comp_choice = random.choice(item_list)

print(f"user choice = {user_choice} , computer_choice = {comp_choice}")


if(user_choice == comp_choice):
    print("Both choose same := Match Tie")
elif user_choice == "rock":
    if(comp_choice == "paper"):
        print("paper wins")
    else:
         print("scissors wins")
         
elif user_choice == "scissors":
    if(comp_choice == "paper"):
        print("scissors wins")
    else:
        print("rock wins")
else: 
    if comp_choice == "scissors":
        print("scissors wins")
    else:
        print("paper wins")