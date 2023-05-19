from data import *

# GET BET 
def get_bet():
    """
    Asks the player to enter the bet amount.
    """
    while True:
        amount = input("What would you like to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

# GET LINES
def get_number_of_lines():
    """
    Asks the player to choose the number of lines they want to bet on.
    """
    while True:
        lines = input(f"On how many lines would you like to bet (1-{MAX_LINES})? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number.")
    return lines

