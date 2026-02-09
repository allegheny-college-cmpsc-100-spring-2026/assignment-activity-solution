import random

from time import sleep
from machine import Pin

def generate(items: int = random.randint(5, 10)) -> list:
    """
    Generates a list of unique numbers
    
    :param items: Description
    :type items: int
    :return: Description
    :rtype: list
    """
    return list(
        set(
            [random.randint(1,items) for _ in range(items)]
        )
    )

def reset_instruction() -> list:
    """
    Reusable list resetting
    
    :return: Description
    :rtype: list
    """
    return []

def press(btn: Pin) -> str:
    """
    Determines what kind of press we recieve
    
    :param btn: Description
    :type btn: Pin
    :return: Description
    :rtype: str
    """
    seconds = 0
    while btn.value() == 0:
        seconds += .2
        sleep(.15)
    if .1 < seconds < .5:
        return "short"
    if .5 < seconds:
        return "long"

def select(values: list = [], choice: list = []) -> list:
    """
    Swaps the numbers that we select
    
    :param values: Description
    :type values: list
    :param choice: Description
    :type choice: list
    :return: Description
    :rtype: list
    """
    swap_from = values[choice[0] - 1]
    swap_with = values[choice[1] - 1]
    values[choice[0] - 1] = swap_with
    values[choice[1] - 1] = swap_from
    return values

def main(values: list = []):

    btn = Pin(16, Pin.IN, Pin.PULL_UP)
    led = Pin("LED", Pin.OUT)

    print(f"Starting values: {values}")

    instruction = reset_instruction()
    short, count = 0, 0

    while not sorted(values) == values:

        if len(instruction) == 2:
            values = select(values = values, choice = instruction)
            instruction = reset_instruction()
            print(f"New values: {values}")

        if btn.value() == 0:
            led.on()
            signal = press(btn = btn)

            if signal == "long" and len(instruction) > 1:
                instruction = reset_instruction()
                print("RESET")
                continue

            elif signal == "long":
                instruction.append(count)
                count = 0
                print(instruction)
            
            if signal == "short":
                count += 1

            sleep(.15)
        led.off()

if __name__ == "__main__":
    random_list = generate()
    main(random_list)