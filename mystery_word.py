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
            sleep(.05)
    else:
        print(a_string)



###############################
####   WHILE LOOP STARTS   ####
###############################


def select_difficulty():
    difficulty = input("Please select a difficulty:\n\n[E]asy: 4 - 6 characters\n[N]ormal: 6 - 8\n[H]ard:8+ \n>").lower()

    if is_difficulty_valid(difficulty):
        return difficulty
    else:
        print("*" * 40 + "\n")
        print("Please only type 'e', 'n', or 'h'.\n")
        print("*" * 40 + '\n')
        return select_difficulty()


def is_difficulty_valid(difficulty):
    if difficulty != 'e' and difficulty != 'n' and difficulty != 'h' or len(difficulty) > 1:
        clear()
        return False
    else:
        return True




def get_word_from_file(difficulty):
    mystery_word = ''
    difficulty_dict = get_difficulty_lists()
    clear()
    print("*" * 40)
    if difficulty == 'e':
        print("\nYou have chosen Easy mode.")
        mystery_word = random.choice(difficulty_dict['e'])
    elif difficulty == 'n':
        print("\nYou have chosen Normal mode.")
        mystery_word = random.choice(difficulty_dict['n'])
    elif difficulty == 'h':
        print("\nYou have chosen Hard mode.")
        mystery_word = random.choice(difficulty_dict['h'])
    return (mystery_word.upper()).rstrip()



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



def tell_how_many_letters(mystery_word):
    print("\nYour word is {} letters long. Good luck!\n".format(len(mystery_word)))




###########################
####   Guess & Check   ####
###########################



def get_user_guess(mystery_word, guessed_letters, guesses_left):
    print("*" * 40)

    if guesses_left < 8:
        guess = input("\nPlease enter your guess. You have {} chances left.\n".format(guesses_left))
    else:
        guess = input("\nPlease enter your guess. You have {} chances.\n".format(guesses_left))
    guess = guess.upper()

    if is_guess_valid(mystery_word, guess, guessed_letters):
        return guess
    else:
        return get_user_guess(mystery_word, guessed_letters, guesses_left)


def is_guess_valid(mystery_word, guess, guessed_letters):
    if not is_guess_too_long(mystery_word, guess, guessed_letters):
        return False
    elif not is_guess_a_letter(mystery_word, guess, guessed_letters):
        return False
    elif not has_been_guessed(mystery_word, guess, guessed_letters):
        return False
    else:
        return True


def is_guess_a_letter(mystery_word, guess, guessed_letters):
    if not guess.isalpha() or guess == '':
        clear()
        print("*" * 40)
        print("\nOnly enter letters. Try again.\n\nThe word is {} letters long.\nSo far, you have guessed: {}\n".format(len(mystery_word), ", ".join(guessed_letters)))
        return False
    else:
        return True

def is_guess_too_long(mystery_word, guess, guessed_letters):
    if len(guess) > 1:
        clear()
        print("*" * 40)
        print("\nPlease only guess one letter at a time.\n\nThe word is {} letters long.\nSo far, you have guessed: {}\n".format(len(mystery_word), ", ".join(guessed_letters)))
        return False
    else:
        return True

def has_been_guessed(mystery_word, guess, guessed_letters):
    if guess in guessed_letters:
        clear()
        print("*" * 40)
        print("\nYou already tried that letter.\n\nThe word is {} letters long.\nSo far, you have guessed: {}\n".format(len(mystery_word), ", ".join(guessed_letters)))
        return False
    else:
        return True


#################################
####   Checking for Match    ####
#################################


def is_match_in_word(mystery_word, guess):

    if guess in mystery_word:
        return True
    else:
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
        draw_line_eight(incorrect)
    print("*" * 40)


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
    print_word(mystery_word, guessed_letters, word_so_far)
    draw_hangman(incorrect)



def print_word(mystery_word, guessed_letters, word_so_far):
    if len(mystery_word) == 0:
        print_text("".join(word_so_far) + '\n', True,)
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


def show_winner(mystery_word, guessed_letters, word_so_far, incorrect):
    print("\nYou got it in {} guesses! Congrats!\nThe word was {}.\n\n".format(len(guessed_letters), mystery_word))
    print("*" * 40 + '\n')

def print_loss_message(mystery_word, guessed_letters, word_so_far, incorrect):
    print("\nSorry you didn't get it this time.\n\n\nThe word was {}.\n\n".format(mystery_word))
    print("*" * 40 + '\n')





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

    tell_how_many_letters(mystery_word)

    while True:
        guess = get_user_guess(mystery_word, guessed_letters, guesses_left)
        print("After full guess function, get guess guessed letters: ", guessed_letters)
        print("After full get guess guess: ", guess)

        word_so_far = []
        guessed_letters.append(guess)
        print("After append guessed letters: ", guessed_letters)


        if not is_match_in_word(mystery_word, guess):
            guesses_left -= 1
            incorrect += 1
            clear()
            print(("*" * 40) + "\nSorry, that isn't one of the letters. Try again!\n\nSo far, you have guessed: {}\n".format(", ".join(guessed_letters)))
            print("*" * 40 + '\n')
            display_word_with_guesses(mystery_word, guessed_letters, word_so_far, incorrect)

        else:
            clear()
            print(("*" * 40) + "\nYeah! That one is in there. Keep it up!\n\nSo far, you have guessed: {}\n".format(", ".join(guessed_letters)))
            print("*" * 40 + '\n')
            display_word_with_guesses(mystery_word, guessed_letters, word_so_far, incorrect)

        if check_for_win(mystery_word, guessed_letters):
            show_winner(mystery_word, guessed_letters, word_so_far, incorrect)
            break
        elif guesses_left <= 0:
            print_loss_message(mystery_word, guesses_left, word_so_far, incorrect)
            break

    if go_again() == True:
        main()

    clear()

if __name__ == '__main__':
    main()
