from typing import List
import random


def pick_random_word_from_text_file(file: str) -> str:
    """ Picks a random word from a text file given.

    Args:
        file: Path to the text file.

    Returns:
        Random word.
    """
    with open(file, "r") as f:
        lines = [line.strip() for line in f]

    random_word = random.choice(lines)

    return random_word


def hangman_game(random_word):

    print("Welcome to the hangman game")
    solution = random_word
    solution = list(solution)
    used_letters = set()
    word = ["_" for x in range(len(solution))]
    tries = 0
    while True:
        draw_game(tries)
        print(" ".join(word))

        if tries == 6:
            print(f"You are a looser: {''.join(solution)}")
            break

        letter = input("Introduce a letter: ")
        letter = letter.upper()

        if letter in used_letters:
            print("You have already used this letter")
            continue

        used_letters.add(letter)

        if letter in solution:
            word = replace_letter_in_word(word, letter, solution)

            if word == solution:
                print(f"You've guessed the word: {''.join(solution)}")
                break
        else:
            print("Try with another letter")
            tries += 1


def replace_letter_in_word(word: List[str], letter: str, solution: List[str]) -> List[str]:
    """ Replaces the letter in the empty word if the letter is in the solution.
    Args:
        word: A list empty of letters.
        letter: A letter given by the player.
        solution: A list with the letters of the solution.

    Returns:
        The word updated.
    """

    for i in range(len(solution)):
        if solution[i] == letter:
            word[i] = letter
    return word


def draw_game(tries: int) -> None:
    """ Draws the hangman game with the tries given.
    Args:
        tries: It's the number of tries that the player has left.

    """
    full_hangman = ["O", "|", "/", "\\", "/", "\\"]
    hangman = [" " for _ in range(len(full_hangman))]

    for i in range(tries):
        hangman[i] = full_hangman[i]

    print(" ______")
    print(" |    |")
    print(f" |    {hangman[0]}")
    print(f" |   {hangman[2]}{hangman[1]}{hangman[3]}")
    print(f" |   {hangman[4]} {hangman[5]}")
    print("---")


if __name__ == "__main__":
    hangman_game(pick_random_word_from_text_file("src/sowpods.txt"))