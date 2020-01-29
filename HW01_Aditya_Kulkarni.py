"""
Implemented a Rock/Paper/Scissor game where user plays with computer
who randomly selects one option to play
"""
from random import choice


def play_game() -> None:
    """
    Play the game,
    ask user for input of their choice,
    compare it with the computer's move
    and then print the outcome
    """
    options: dict = {'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Paper'}
    mappings: dict = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
    while True:
        human_move: str = input("Choose your option 'R', 'P', 'S' or 'Q' for quitting: ").upper()
        computer_move: str = choice(list(mappings.keys()))
        #Checking for quit, invalid inputs and tie breakers
        if human_move == 'Q':
            print("Let's play later")
            break
        elif human_move not in mappings:
            print("Cannot recognize this input")
            continue
        elif mappings[human_move] == mappings[computer_move]:
            print(f"It's a tie. {mappings[human_move]} -> {mappings[computer_move]}. Wanna try again? ")
        else:
            #Checking for winner 
            if options[mappings[human_move]] == mappings[computer_move]:
                print(f"Awesome! You've won. {mappings[human_move]} -> {mappings[computer_move]}")
            else:
                print(f"Aw shucks! You lost. {mappings[computer_move]} -> {mappings[human_move]}")


if __name__ == '__main__':
    play_game()
