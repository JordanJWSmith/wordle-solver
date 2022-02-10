def check_green(green_dict, word):
    if not len(green_dict):
        return True
    return all([letter in word and word.index(letter) == green_dict[letter] for letter in green_dict.keys()])


def check_yellow(yellow_dict, word):
    if not len(yellow_dict):
        return True
    word_dict = {letter: word.count(letter) for letter in yellow_dict}
    return all([yellow_dict[letter] <= word_dict[letter] for letter in yellow_dict])






