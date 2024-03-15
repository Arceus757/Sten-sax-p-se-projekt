import random
from colors import bcolors

# Funktion för att bestämma vinnaren av en runda
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Tie"
    elif (player_choice == 'r' and computer_choice == 's') or \
         (player_choice == 'p' and computer_choice == 'r') or \
         (player_choice == 's' and computer_choice == 'p'):
        return "Player"
    else:
        return "Computer"

# Funktion för att skriva ut symbolen för spelarens val
def print_player_choice(choice):
    if choice == 'r':
        print(bcolors.YELLOW + "   _______")
        print(" -'   ____)")
        print("    (_____)")
        print("    (_____)")
        print("    (____)")
        print(" -' (___)")
        print("")
    elif choice == 'p':
        print(bcolors.YELLOW + "    _______ ")
        print("---'   ____)____")
        print("          ______)")
        print("          _______)")
        print("         _______)")
        print("---.__________)")
        print("")
    elif choice == 's':
        print(bcolors.YELLOW +"   _______")
        print(" -'   ____)____")
        print("          ______)")
        print("       __________)")
        print("      (____)")
        print(" -' (___)")
        print("")

# Funktion för att skriva ut symbolen för datorns val
def print_computer_choice(choice):
    if choice == 'r':
        print(bcolors.YELLOW + "   _______")
        print(" -'   ____)----")
        print("        ______)")
        print("      _______)")
        print("     _______)")
        print("---.________)")
        print("")
    elif choice == 'p':
        print(bcolors.YELLOW + "    _______     ")
        print("---'   ____)____")
        print("          ______)")
        print("       __________)")
        print("      (____)")
        print("---.__(___)")
        print("")
    elif choice == 's':
        print(bcolors.YELLOW + "   _______")
        print(" -'   ____)____")
        print("          ______)")
        print("       __________)")
        print("      (____)")
        print("---.__(___)")
        print("")

# Funktion för att hantera en enskild runda av spelet
def play_round(player_choice, wins, losses, ties):
    choices = ['r', 'p', 's']
    computer_choice = random.choice(choices)
    
    print("\nYour choice:")
    print_player_choice(player_choice)
    
    print("Computer's choice:")
    print_computer_choice(computer_choice)
    
    winner = determine_winner(player_choice, computer_choice)
    if winner == "Player":
        print(bcolors.GREEN + "You win this round!")
        wins[0] += 1
    elif winner == "Computer":
        print(bcolors.RED + "Computer wins this round!")
        losses[0] += 1
    else:
        print(bcolors.DEFAULT + "It's a tie!")
        ties[0] += 1
    print(bcolors.DEFAULT + f"| Wins: {wins[0]} | Losses: {losses[0]} | Ties: {ties[0]} |")

# Huvudfunktionen för att köra spelet
def rock_paper_scissors():
    wins = [0]
    losses = [0]
    ties = [0]
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice: 'rock(r)', 'paper(p)', or 'scissors(s)'. To quit, type 'q'.")
    
    while True:
        player_choice = input("Your choice: ").lower()
        
        if player_choice in ['r', 'p', 's']:
            play_round(player_choice, wins, losses, ties)
        elif player_choice == 'q':
            print(bcolors.GREEN + "| Thanks for playing! |")
            print(f"Total wins:| {wins[0]} |, Total losses:| {losses[0]} |, Total ties:| {ties[0]} |")
            break
        else:
            print(bcolors.RED + "Invalid choice. Please choose 'rock(r)', 'paper(p)', 'scissors(s)', or 'quit(q)'.")

# Köra spelet
rock_paper_scissors()
