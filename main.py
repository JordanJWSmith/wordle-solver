from functions.helpers import check_green, check_yellow, clear_console
from functions.inputs import get_green, get_yellow, get_grey


def main():
    with open("dictionary/five_dict.txt", 'r') as f:
        dictionary = f.read()

    dictionary = [word for word in dictionary.split('\n')]

    alphabet = "qwertyuiopasdfghjklzxcvbnm"

    clear_console()
    green_letters = get_green()
    yellow_letters = get_yellow()
    grey_letters = get_grey()

    green_dict = {index: letter for index, letter in enumerate(green_letters) if letter in alphabet}
    yellow_dict = {letter: yellow_letters.count(letter) for letter in yellow_letters}

    alphabet = alphabet.translate(str.maketrans({char: None for char in grey_letters}))

    words = [
        word for word in dictionary if not set(word) - set(alphabet)
        and check_green(green_dict, word)
        and check_yellow(yellow_dict, word)
    ]

    if not len(words):
        print('\nThere are no possible words.')
    else:
        print("\nHere's a list of possible words: ")
        for index, word in enumerate(words):
            print(f"{index+1}: {word}")


if __name__ == '__main__':
    main()