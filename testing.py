guess = 'r'
mystery_word = 'farmer'
word = []

def print_word(mystery_word, guess, word):
    if len(mystery_word) == 0:
        print("".join(word))
        return ''

    for letter in mystery_word:
        print("Ran again")
        if guess == mystery_word[0]:
            word.append(" " + guess.upper() + " ")
            return print_word(mystery_word[1:], guess, word)
        else:
            word.append(" ___ ")
            return print_word(mystery_word[1:], guess, word)
        print("".join(word))


print_word(mystery_word, guess, word)
