import random

print("Rock-paper-scissors, 1, 2 ,3")
random_word = random.choice(['rock', 'paper', 'scissors'])

while True: 
    player_choice = input("Enter your choice (1 for rock, 2 for paper, 3 for scissors): ")
    
    if player_choice not in ['1', '2', '3']:
        print("Invalid input. Please enter a number between 1 and 3.")
        continue
    
    player_choice = int(player_choice)
    
    if player_choice == 1:
        player_choice_str = 'rock'
    elif player_choice == 2:
        player_choice_str = 'paper'
    else:
        player_choice_str = 'scissors'
    
    print(f"You chose {player_choice_str}. Computer chose {random_word}.")
    
    if player_choice_str == random_word:
        print("It's a tie!")
    elif (player_choice_str == 'rock' and random_word == 'scissors') or \
         (player_choice_str == 'paper' and random_word == 'rock') or \
         (player_choice_str == 'scissors' and random_word == 'paper'):
        print("You win!")