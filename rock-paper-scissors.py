import random as rd

choices = ("rock", "paper", "scissors")
u_choice = int(input("1 for rock, 2 for pape, and 3 for scissors: ")) - 1
while(u_choice not in [0, 1, 2]):
    if u_choice not in [0, 1, 2]:
        print("Invalid choice. Please choose 1, 2, or 3.")
    u_choice = int(input("1 for rock, 2 for pape, and 3 for scissors: ")) - 1
else:
    ai_choice = rd.choice(choices)
    print(f"\nYour choice is: {choices[u_choice]}\nAI's choice is: {ai_choice}\n")
    if ai_choice == choices[u_choice]:
        print("It's a draw!")
    elif (choices[u_choice] == "rock" and ai_choice == "scissors") or \
         (choices[u_choice] == "scissors" and ai_choice == "paper") or \
         (choices[u_choice] == "paper" and ai_choice == "rock"):
        print("You win!")
    else:
        print("You lose!")