mystery_word = 'john'
guessed_letters = ['k', 'j']
incorrect = 0
word_so_far = []

def display_word_with_guesses(mystery_word, guessed_letters, word_so_far, incorrect):
    length = len(mystery_word)
    draw_hangman(incorrect)
    print_word(mystery_word, guessed_letters, word_so_far)

display_word_with_guesses(mystery_word, guessed_letters, word_so_far, incorrect)


def draw_hangman(incorrect):
    print("in draw hangman incorrect is: ", incorrect)
    if incorrect <= 0:
        print("\n" * 6)
    else:
        draw_line_one(incorrect)
        draw_line_two(incorrect)
        draw_line_three(incorrect)
        draw_line_four(incorrect)
        draw_line_five(incorrect)
        draw_line_six(incorrect)
        draw_line_seven(incorrect)
        draw_line_eight(incorrect)
    print("*" * 30 + "\n")


def draw_line_one(incorrect):
    if incorrect > 2:
        print((" " * 14) + ("_" * 5))
    else:
        print('')

def draw_line_two(incorrect):
    if incorrect > 1:
        if incorrect > 3:
            print((" " * 14) + "|" + (" " * 4) + "|")
        else:
            print((" " * 19) + "|")
    else:
        print("")

def draw_line_three(incorrect):
    if incorrect > 4:
        print((" " * 14) + "O" + (" " * 4) + "|")
    elif incorrect > 1:
        print((" " * 19) + "|")
    else:
        print("")

def draw_line_four(incorrect):
    if incorrect > 1:
        if incorrect > 6:
            print((" " * 13) + "/|\\" + (" " * 3) + "|")
        elif incorrect > 5:
            print((" " * 14) + "|" + (" " * 4) + "|")
        else:
            print((" " * 19) + "|")

def draw_line_five(incorrect):
    if incorrect > 5:
        print((" " * 14) + "|" + (" " * 4) + "|")
    elif incorrect > 1:
        print((" " * 19) + "|")


def draw_line_six(incorrect):
    if incorrect > 1:
        if incorrect > 7:
            print((" " * 13) + "/ \\" + (" " * 3) + "|")
        else:
            print((" " * 19) + "|")
    else:
        print("")


def draw_line_seven(incorrect):
    if incorrect > 0:
            print((" " * 13) + "______|__")
    else:
        print('')

def draw_line_eight(incorrect):
    if incorrect > 0:
        print(("_" * 12) + "|_________|  ")
    else:
        print("_" * 20)




def display_word_with_guesses(mystery_word, guessed_letters, word_so_far, incorrect):
    length = len(mystery_word)
    draw_hangman(incorrect)
    print_word(mystery_word, guessed_letters, word_so_far)


def print_word(mystery_word, guessed_letters, word_so_far):
    if len(mystery_word) == 0:
        print("".join(word_so_far))
        return ''

    for letter in mystery_word:
        if mystery_word[0] in guessed_letters:
            word_so_far.append("  " + letter.upper() + "  ")
            return print_word(mystery_word[1:], guessed_letters, word_so_far)
        elif mystery_word[0] not in guessed_letters:
            word_so_far.append(" __ ")
            return print_word(mystery_word[1:], guessed_letters, word_so_far)
