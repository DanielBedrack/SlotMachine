from manager import get_deposit, spin, play_again 

def main():
    """
    Entry point of the program. Manages the game flow.
    """
    balance = get_deposit()
    while True:
        print(f"Current balance is ${balance}")
        if balance > 0:
            answer = input("Press enter to play (q to quit).")
            if answer == "q":
                break
            balance += spin(balance)
        else:
            answer = play_again(balance)
            if answer == False:
                break
            else:
                main()
    
main()
