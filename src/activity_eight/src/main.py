import random
from typing import Literal

Move = Literal["rock", "paper", "scissors", "lizard", "spock"]
VALID_MOVES = ("rock", "paper", "scissors", "lizard", "spock")


def normalize_move(value: int) -> str:
    if value > len(VALID_MOVES):
        return "invalid"
    return VALID_MOVES[value - 1]


def decide_winner(player: Move, computer: Move) -> str:
    """Decide winner: 'player', 'computer', or 'tie'."""
    if player == computer:
        return "tie"

    wins = {
        "rock": ("scissors", "lizard"),
        "paper": ("rock", "spock"),
        "scissors": ("paper", "lizard"),
        "lizard": ("spock", "paper"),
        "spock": ("scissors", "rock"),
    }

    return "player" if computer in wins[player] else "computer"


def main() -> None:
    print("Welcome to Rock, Paper, Scissors, Lizard, Spock")

    player_wins = 0
    computer_wins = 0
    ties = 0

    while True:
        print(
            """Enter a move:
1.  Rock
2.  Paper
3.  Scissors
4.  Lizard
5.  Spock
6.  Exit
"""
        )
        user_input = int(input(":"))
        if user_input == 6:
            print("Thanks for playing")
            break
        normalized = normalize_move(user_input)

        if normalized == "invalid":
            print("Invalid move. Please enter rock, paper, scissors, lizard, or spock.")
            continue

        computer_move = random.choice(VALID_MOVES)
        winner = decide_winner(normalized, computer_move)

        print(f"You chose: {normalized}")
        print(f"Computer chose: {computer_move}")

        if winner == "tie":
            ties += 1
            print("It's a tie!")
        elif winner == "player":
            player_wins += 1
            print("You win!")
        else:
            computer_wins += 1
            print("Computer wins!")

        print(f"Score - You: {player_wins}, Computer: {computer_wins}, Ties: {ties}")

        if abs(player_wins - computer_wins) >= 5:
            leader = "You" if player_wins > computer_wins else "Computer"
            print(f"MERCY RULE INVOKED: {leader} wins.")
            break


if __name__ == "__main__":
    main()
