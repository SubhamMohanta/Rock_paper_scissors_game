import random

def generate_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "Player wins!"
    else:
        return "Computer wins!"

def play_round(player_name):
    print(f"{player_name}, choose your hand:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    player_choice = input("Enter your choice: ").lower()
    
    while player_choice not in ["1", "2", "3", "rock", "paper", "scissors"]:
        print("Invalid choice. Please choose again.")
        player_choice = input("Enter your choice: ").lower()
    
    computer_choice = generate_computer_choice()
    
    outcome = determine_winner(player_choice, computer_choice)
    
    print(f"{player_name} choice:", player_choice)
    print("Computer choice:", computer_choice)
    print(outcome)
    
    return outcome

def rock_paper_scissors():
    player_name = input("Enter your name: ").strip()
    while not player_name:
        print("Please enter a valid name.")
        player_name = input("Enter your name: ").strip()
    
    num_rounds = int(input("Enter the number of rounds you want to play: "))
    
    player_score = 0
    computer_score = 0
    
    for _ in range(num_rounds):
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
