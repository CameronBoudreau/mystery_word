import os
import random
from time import sleep
import sys


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# displays text as if someone is typing
def print_text(a_string, a_is_slow):
    if a_is_slow:
        for words in a_string + "\n":
            sys.stdout.write(words)
            sys.stdout.flush()
            sleep(.03)
    else:
        print(a_string)



###############################
####   WHILE LOOP STARTS   ####
###############################


def select_difficulty():
    difficulty = input("Please select a difficulty:\n\n[E]asy: 4 - 6 characters\n[N]ormal: 6 - 8\n[H]ard:8+ \n>").lower()

    if difficulty != 'e' and difficulty != 'n' and difficulty != 'h':
        clear()
        print("*" * 30 + "\n")
        print("Please only type 'e', 'n', or 'h'.\n")
        print('*' * 30)
        return select_difficulty()

    return difficulty



def get_word_from_file(difficulty):
    mystery_word = ''
    difficulty_dict = get_difficulty_lists()

    if difficulty == 'e':
        mystery_word = random.choice(difficulty_dict['e'])
    elif difficulty == 'n':
        mystery_word = random.choice(difficulty_dict['n'])
    elif difficulty == 'h':
        mystery_word = random.choice(difficulty_dict['h'])
    return (mystery_word.lower()).rstrip()



def get_difficulty_lists():

    with open('/usr/share/dict/words', 'r') as f:
        easy_list = get_easy(f)
        f.seek(0)
        normal_list = get_normal(f)
        f.seek(0)
        hard_list = get_hard(f)

        difficulty_dict = {
        'e':easy_list,
        'n':normal_list,
        'h':hard_list
        }

    return difficulty_dict


def get_easy(f):
    easy_list = []

    for line in f:
        if 4 <= len(line) <= 6:
            easy_list.append(line)
    return easy_list


def get_normal(f):
    normal_list = []

    for line in f:
        if 6 <= len(line) <= 8:
            normal_list.append(line)
    return normal_list


def get_hard(f):
    hard_list = []

    for line in f:
        if len(line) >= 8:
            hard_list.append(line)
    return hard_list



def tell_how_many_letters(mystery_word, difficulty):
    clear()
    print("*" * 30)
    if difficulty == 'e':
        print("\nYou have chosen Easy mode.")
    if difficulty == 'n':
        print("\nYou have chosen Normal mode.")
    if difficulty == 'h':
        print("\nYou have chosen Hard mode.")
    print("Your word is {} letters long. Good luck!\n".format(len(mystery_word)))




###########################
####   Guess & Check   ####
###########################


def get_user_guess(guessed_letters, guesses_left):
    print("*" * 30)
    if guesses_left < 8:
        guess = input("\nPlease enter your guess. You have {} chances left.\nSo far, you have guessed: {}\n\n".format(guesses_left, ", ".join(guessed_letters)))
    else:
        guess = input("\nPlease enter your guess. You have {} chances.\n".format(guesses_left))

    clear()
    if is_guess_a_letter(guess, guessed_letters, guesses_left):
        return get_user_guess(guessed_letters, guesses_left)
    elif test_guess_length(guess, guessed_letters, guesses_left):
        return get_user_guess(guessed_letters, guesses_left)
    elif has_been_guessed(guess, guessed_letters, guesses_left):
        return get_user_guess(guessed_letters, guesses_left)
    return guess


def is_guess_a_letter(guess, guessed_letters, guesses_left):
    if not guess.isalpha() or guess == '':
        clear()
        print("*" * 30)
        print("\nOnly enter letters. Try again.\n")
        return True


def test_guess_length(guess, guessed_letters, guesses_left):
    if len(guess) > 1:
        clear()
        print("*" * 30)
        print("\nPlease only guess one letter at a time.\n")
        return True


def has_been_guessed(guess, guessed_letters, guesses_left):
    if guess in guessed_letters:
        clear()
        print("*" * 30)
        print("\nYou already tried that letter.\n")
        return True



#################################
####   Checking for Match    ####
#################################


def check_and_print_match_in_word(mystery_word, guess, guessed_letters, guesses_left, word_so_far):
    if guess in mystery_word:
        print("Yeah! That one is in there. Keep it up!\n\nSo far, you have guessed: {}\n".format(", ".join(guessed_letters)))
        display_word_with_guesses(mystery_word, guessed_letters, word_so_far)
        return True
    else:
        print("Sorry, that's incorrect.\n\nSo far, you have guessed: {}\n".format(", ".join(guessed_letters)))
        display_word_with_guesses(mystery_word, guessed_letters, word_so_far)
        return False


##########################
####   Display Game   ####
##########################


def draw_hangman(incorrect):
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
    print("_" * 30)

def draw_line_one(incorrect):
    if incorrect > 2:
        print((" " * 14) + ("_" * 5)
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
    elif incorrect > 2:
        print((" " * 19) + "|")
    else:
        print("")
def draw_line_four(incorrect):
    if incorrect > 2:
        if incorrect > 5:
            print((" " * 14) + "|" + (" " * 4) + "|")
        elif incorrect > 6:
            print((" " * 13) + "\|/" + (" " * 3) + "|")
        else:
            print("")

def draw_line_five(incorrect):
    if incorrect > 2:
        if incorrect > 7:
            print((" " * 9) + "/\\" + (" " * 3) + "|")
        else:
            print((" " * 14) + "|")
    else:
        print("")
def draw_line_six(incorrect):
    if incorrect > 0:
        if incorrect > 2:
            print((" " * 14) + "|")
        else:
            print((" " * 13) + "____")
    else:
        print('')

def draw_line_seven(incorrect):
    if incorrect > 0:
        print(("_" * 13) + "|__" + "__|  "
    else:
        print("_" * 20)


def display_word_with_guesses(mystery_word, guessed_letters, word_so_far):
    length = len(mystery_word)
    print(('*' * (length * 4 + 4)))
    print(('|' + " " * (length * 4 + 2) + ('|\n')) * 6, end='')
    print('| ', end='')
    print_word(mystery_word, guessed_letters, word_so_far)


def print_word(mystery_word, guessed_letters, word_so_far):
    if len(mystery_word) == 0:
        print("".join(word_so_far) + ' |')
        return ''

    for letter in mystery_word:
        if mystery_word[0] in guessed_letters:
            word_so_far.append("  " + letter.upper() + "  ")
            return print_word(mystery_word[1:], guessed_letters, word_so_far)
        elif mystery_word[0] not in guessed_letters:
            word_so_far.append(" __ ")
            return print_word(mystery_word[1:], guessed_letters, word_so_far)



#######################
####   Win Check   ####
#######################


def check_for_win(mystery_word, guessed_letters):
    number_correct = 0

    for letter in mystery_word:
        if letter in guessed_letters:
            number_correct += 1
        if number_correct == len(mystery_word):
            return True



def show_winner(guesses_left):
    print("You got it in {} guesses! Congrats!\n".format(8 - guesses_left))


def print_loss_message(mystery_word, guessed_letters):
    print("Sorry you didn't get it this time.\n\nYou guessed these letters:\n{}\nThe word was ".format(guessed_letters), mystery_word.upper(), '\n')



####################
####   Again?   ####
####################



def go_again():
    again = input("Would you like to go again? [y/N] \n")
    if again.lower() == 'y':
        return True



##################
####   Main   ####
##################


def main():
    clear()

    guess = ''
    guessed_letters = []
    difficulty = 0
    guesses_left = 8
    word_so_far = []
    incorrect = 0

    difficulty = select_difficulty()

    mystery_word = get_word_from_file(difficulty)

    tell_how_many_letters(mystery_word, difficulty)

    while True:
        guess = get_user_guess(guessed_letters, guesses_left)
        word_so_far = []
        guessed_letters.append(guess)

        if not check_and_print_match_in_word(mystery_word, guess, guessed_letters, guesses_left, word_so_far):
            guesses_left -= 1
            incorrect += 1
        if check_for_win(mystery_word, guessed_letters):
            show_winner(guesses_left)
            break
        elif guesses_left <= 0:
            print_loss_message(mystery_word, guesses_left)
            break

    if go_again() == True:
        main()

    clear()

if __name__ == '__main__':
    main()
