import random
from typing import Literal

Move = Literal["rock", "paper", "scissors", "lizard", "spock"]
VALID_MOVES = ("rock", "paper", "scissors", "lizard", "spock")


def normalize_move(value: str) -> str:
    return value.strip().lower()


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


def play_round(player_input: str) -> tuple[str, str, str]:
    """Play one round and return (player_move, computer_move, winner)."""
    player = normalize_move(player_input)
    if player not in VALID_MOVES:
        raise ValueError(f"Invalid move: {player_input}")

    computer = random.choice(VALID_MOVES)
    winner = decide_winner(player, computer)
    return player, computer, winner


def main() -> None:
    print("Welcome to Rock, Paper, Scissors, Lizard, Spock")
    print("Type 'quit' to exit")

    player_wins = 0
    computer_wins = 0
    ties = 0

    while True:
        user_input = input("Enter move (rock/paper/scissors/lizard/spock): ")
        normalized = normalize_move(user_input)

        if normalized == "quit":
            print("Thanks for playing")
            break

        if normalized not in VALID_MOVES:
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
