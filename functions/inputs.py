def get_green():
    print(
        '\n'
        'Enter the current word so far. \n'
        'Where the letter is green, enter the letter. Otherwise, use an underscore (_). \n'
        'For example, if you have two green letters (c and e) in positions 4 and 5, enter ___ce. \n'
        'If you have no green letters, enter _____.'
    )

    while True:
        green_letters = input('Word: ').lower()
        if len(green_letters) != 5:
            print('Input must be five spaces long.\n')
            continue
        elif not is_alpha(green_letters):
            print('You used an invalid character.\n')
            continue
        else:
            break

    return green_letters


def get_yellow():
    print(
        '\n'
        'Enter any yellow letters. \n'
        'For example, if you know the letters f, a and l are in the word but are highlighted as yellow, '
        'enter fal.\n'
        'If you don\'t have any yellow letters, just press enter.'
    )

    while True:
        yellow_letters = input('Yellow Letters: ').lower()
        if len(yellow_letters) > 5:
            print('You entered too many characters. \n')
            continue
        if not is_alpha(yellow_letters):
            print('You used an invalid character.\n')
            continue
        else:
            break

    return yellow_letters


def get_grey():
    print(
        '\n'
        'Enter any incorrect (grey) letters. \n'
        'For example, if you know the letters x, y and z are definitely not in the word, enter xyz. \n'
        'If you don\'t have any grey letters, just press enter'
    )

    while True:
        grey_letters = input('Grey Letters: ').lower()
        if not is_alpha(grey_letters):
            print('You used an invalid character.\n')
            continue
        else:
            break

    return grey_letters


def is_alpha(word):
    alphabet = "qwertyuiopasdfghjklzxcvbnm"
    return all([char in alphabet or char == '_' for char in word])
