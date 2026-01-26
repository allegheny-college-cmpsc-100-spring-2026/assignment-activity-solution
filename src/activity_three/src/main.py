import random

def message(text: str = "right on") -> str:
    return f"You were {text}!"

def generate(low: int = 1, high: int = 100) -> int:
    return random.randint(low, high)

def make_progressive(guess: int = 1, answer: int = 1) -> int:
    if guess > answer:
        answer = generate(low = answer, high = guess) - 1
    else:
        answer = generate(low = guess, high = answer) + 1
    return answer

def main(answer: int = 1, low: int = 1, high: int = 100, count: int = 1):
    again = True
    right = False

    while again:
        
        guess = int(input(f"Guess a number between {low}-{high}: "))
        # Evaluate answer and guess
        if guess < answer:
            print(message(text = "too low"))
        elif guess > answer:
            print(message(text = "too high"))
        else:
            print(message())
            right = True

        # Evaluate right/wrong, and playing again
        if right:
            print(f"It took you {count} guess(es)")
            # Reset count and "rightness"
            count = 0
            right = False
            again = input("Guess again (y/n)? ").lower() == "y"
            answer = generate(low = low, high = high)
        else:
            count += 1
            # Stretch goal for progressive easing
            answer = make_progressive(guess = guess, answer = answer)
    

if __name__ == "__main__":
    low, high = 1, 100
    answer = generate(low = low, high = high)
    main(answer = answer)