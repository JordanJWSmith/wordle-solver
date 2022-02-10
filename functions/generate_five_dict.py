with open('../dictionary/usa.txt', 'r') as f:
    dictionary = f.read()

dictionary = [word for word in dictionary.split('\n') if len(word) == 5]

five_dictionary = open('../dictionary/five_dict.txt', 'w')

for word in dictionary:
    five_dictionary.write(word + '\n')

five_dictionary.close()


