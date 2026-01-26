import random

def message(text: str = "right on") -> str:
    return f"You were {text}!"

def generate(low: int = 1, high: int = 100) -> int:
    return random.randint(low, high)

def make_progressive(guess: int = 1, answer: int = 1) -> int:
    if guess > answer:
        answer = generate(low = answer, high = guess - 1)
    else:
        answer = generate(low = guess + 1, high = answer)
    return answer

def main(answer: int = 1, low: int = 1, high: int = 100):
    again = True
    right = False
    
    guess = int(input(f"Guess a number between {low}-{high}: "))
    # Evaluate answer and guess
    if guess < answer:
        print(message(text = "too low"))
    elif guess > answer:
        print(message(text = "too high"))
    else:
        print(message())
    
    again = input("Guess again (y/n)? ").lower() == "y"
    # Evaluate right/wrong, and playing again
    if right and again:
        answer = generate(low = low, high = high)
    elif not right and again:
        answer = make_progressive(guess = guess, answer = answer)
    if again:
        main(answer = answer)
    

if __name__ == "__main__":
    low, high = 1, 100
    answer = generate(low = low, high = high)
    main(answer = answer)