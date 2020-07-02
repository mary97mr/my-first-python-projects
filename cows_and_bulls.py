import random
from typing import List, Tuple

def cows_and_bulls():
    print("Welcome to cows and bulls game")
    n_wins = 0
    while True:
        random_num = random.sample(range(0, 10), 4)
        print(random_num)
        while True:
            user_num = list(input("Give me a number of 4 digits: "))
            user_num = [int(x) for x in user_num]
            count_cows, count_bulls = calculate_cows_and_bulls(random_num, user_num)
            print(f"You have: {count_cows} cows and {count_bulls} bulls")
            if count_cows == 4:
                print("Congrats! You guessed the number")
                n_wins += 1
                break
        game_over = input("Enter 'exit' to finish the game or another button to keep playing: ")
        if game_over == "exit":
            print(f"You have guessed {n_wins} times")
            print("Come back soon")
            break


def calculate_cows_and_bulls(list1: List[int], list2: List[int]) -> Tuple[int, int]:
    """ Compares the two lists given to calculate how many cows and bulls there are.
    Args:
        list1: List of numbers generated ramdomly.
        list2: List of numbers that the user has chosen.

    Returns:
        The counts of cows and bulls.

    """
    n_cows = 0
    n_bulls = 0
    assert len(list1) == len(list2)
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            n_cows += 1
        elif list1[i] != list2[i] and list1[i] in list2:
            n_bulls += 1

    return n_cows, n_bulls


if __name__ == "__main__":

    cows_and_bulls()