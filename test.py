import random

def generate_computer_choice():

    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):

    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 1 and computer_choice == 3) or \
         (player_choice == 2 and computer_choice == 1) or \
         (player_choice == 3 and computer_choice == 2):
        return "Player wins!"
    else:
        return "Computer wins!"

def play_round(player_name):

    print(f"{player_name}, choose your hand:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    player_choice = int(input("Enter your choice: "))
    

    while player_choice not in [1, 2, 3]:
        print("Invalid choice. Please choose again.")
        player_choice = int(input("Enter your choice: "))
    

    computer_choice = random.randint(1, 3)
    

    outcome = determine_winner(player_choice, computer_choice)
    

    print(f"{player_name} choice:", player_choice)
    print("Computer choice:", computer_choice)
    print(outcome)
    

    return outcome

def rock_paper_scissors():

    player_name = input("Enter your name: ")
    
    player_score = 0
    computer_score = 0
    
    
    for _ in range(3):
        outcome = play_round(player_name)
        if outcome == "Player wins!":
            player_score += 1
        elif outcome == "Computer wins!":
            computer_score += 1
    
    
    print("\nTotal score:")
    print(f"{player_name}:", player_score)
    print("Computer:", computer_score)
    if player_score > computer_score:
        print("You won!")
    elif player_score < computer_score:
        print("Computer wins!")
    else:
        print("It's a tie!")


rock_paper_scissors()
