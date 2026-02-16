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
    led = Pin("LED", Pin.OUT)
    while btn.value() == 0:
        led.on()
        seconds += .2
        sleep(.1)
    led.off()
    if .01 < seconds < .5:
        return "short"
    elif .5 <= seconds:
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
    first = choice[0] - 1
    second = choice[1] - 1
    swap_from = values[first]
    swap_with = values[second]
    values[first] = swap_with
    values[second] = swap_from
    print(values)
    return values



def main(values: list = []):

    btn = Pin(16, Pin.IN, Pin.PULL_UP)

    print(f"Starting values: {values}")
    short, count = 0, 0
    instruction = reset_instruction()
    while values != sorted(values):
        if btn.value() == 0:
            signal = press(btn = btn)
            if signal == "short":
                count += 1
                if len(instruction) == 2:
                    count -= 1
                    #values = select (values, choice)
                    values = select(choice = instruction, values = values)
                    instruction = reset_instruction()
            elif signal == "long":
                instruction.append(count)
                count = 0

            
            

    pass

if __name__ == "__main__":
    random_list = generate()
    main(random_list)
