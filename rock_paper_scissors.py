

def check_option(option: str) -> bool:
    """ Checks if the player uses one of the options or not.

    Args:
        option: A choice of the player.

    Returns:
        True or False, if the player has chosen one of the options.
    """
    if option == "r" or option == "p" or option == "s":
        return True
    else:
        return False


def main():

    while True:

        print("Welcome to rock, paper and scissors")

        player1 = input("Player1, choose between rock (r), paper (p) and scissors (s): ")

        player2 = input("Player2, choose between rock (r), paper (p) and scissors (s): ")

        if not(check_option(player1) and check_option(player2)):
            print("Try again with a valid option")
            continue

        if player1 == player2:
            print("It's a tie")

        elif (player1 == 'r' and player2 == 's') or (player1 == 'p' and player2 == 'r') or (player1 == 's' and player2 == 'p'):
            print("Player1 wins")

        else:
            print("Player2 wins")

        answer = input("Enter 'q' to quit, or anything else to play again: ")

        if answer == "q":
            print("See you soon")
            break


if __name__ == "__main__":
    main()