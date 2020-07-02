import random
import string


def generate_password(len_pass: int, lowercase: bool, uppercase: bool, numbers: bool, symbols: bool) -> str:
    """ Creates a strong and random password with the features the user wants it to be.
    Args:
        len_pass: The length of the password.
        lowercase: If the password will contain lowercase letters or not.
        uppercase: If the password will contain uppercase letters or not.
        numbers: If the password will contain numbers or not.
        symbols: If the password will contain symbols or not.

    Returns:
        A password.
    """

    password = ""

    for i in range(len_pass):
        list_choice = []
        if numbers:
            list_choice.append(generate_number())
        if lowercase:
            list_choice.append(generate_lowercase())
        if uppercase:
            list_choice.append(generate_uppercase())
        if symbols:
            list_choice.append(generate_symbols())

        character = random.choice(list_choice)
        password += character

    return "".join(password)


def generate_number():
    return str(random.randint(0, 9))


def generate_lowercase():
    return random.choice(string.ascii_lowercase)


def generate_uppercase():
    return random.choice(string.ascii_uppercase)


def generate_symbols():

    return random.choice(string.punctuation)


def main():
    print(generate_password(30, True, True, True, True))


if __name__ == "__main__":

    main()





