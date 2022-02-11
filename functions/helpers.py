import os


def check_green(green_dict, word):
    if not len(green_dict):
        return True
    return all([letter in word and green_dict[index] == word[index] for index, letter in green_dict.items()])


def check_yellow(yellow_dict, word):
    if not len(yellow_dict):
        return True
    word_dict = {letter: word.count(letter) for letter in yellow_dict}
    return all([yellow_dict[letter] <= word_dict[letter] for letter in yellow_dict])


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
