import os
import random


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


###############################
####   WHILE LOOP STARTS   ####
###############################


def select_difficulty():
    difficulty = input("Please select a difficulty:\n\n[E]asy: 4 - 6 characters\n[N]ormal: 6 - 8\n[H]ard:8+ \n>").lower()

    if difficulty != 'e' and difficulty != 'n' and difficulty != 'h':
        clear()
        print("Please only type 'e', 'n', or 'h'.\n")
        print('*' * 20)
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
    if difficulty == 'e':
        print("You have chosen Easy mode.")
    if difficulty == 'n':
        print("You have chosen Normal mode.")
    if difficulty == 'h':
        print("You have chosen Hard mode.")
    print("Your word is {} letters long. Good luck!".format(len(mystery_word)))




###########################
####   Guess & Check   ####
###########################


def get_user_guess(guessed_letters, guesses_left):
    if guesses_left < 8:
        print("Top of guess: ", guessed_letters)
        guess = input("Please enter your guess. You have {} chances left.\nSo far, you have guessed: {}\n\n".format(guesses_left, guessed_letters))
    else:
        guess = input("Please enter your guess. You have {} chances.\n".format(guesses_left))

    if is_guess_a_letter(guess, guessed_letters, guesses_left):
        get_user_guess(guessed_letters, guesses_left)
    if test_guess_length(guess, guessed_letters, guesses_left):
        get_user_guess(guessed_letters, guesses_left)
    if has_been_guessed(guess, guessed_letters, guesses_left):
        get_user_guess(guessed_letters, guesses_left)
    print("end of get guess: ", guess)
    return guess


def is_guess_a_letter(guess, guessed_letters, guesses_left):
    if not guess.isalpha() or guess == '':
        clear()
        print("Only enter letters. Try again.")
        return True


def test_guess_length(guess, guessed_letters, guesses_left):
    if len(guess) > 1:
        clear()
        print(guessed_letters)

        print("Please only guess one letter at a time.")
        return True


def has_been_guessed(guess, guessed_letters, guesses_left):
    if guess in guessed_letters:
        clear()
        print("You already tried that letter.\n")
        print("So far you have guessed:")
        print(" ".join(guessed_letters), "\n")
        print(('*' * 20) + '\n\n')
        return True



#################################
####   Checking for Match    ####
#################################


def check_and_print_match_in_word(mystery_word, guess, guessed_letters, guesses_left, word_so_far):
    if guess in mystery_word:
        print("Yeah! That one is in there. Keep it up!\n\n")
        display_word_with_guesses(mystery_word, guessed_letters, word_so_far)
        return True
    else:
        print("Sorry, that's incorrect.\n\n")
        display_word_with_guesses(mystery_word, guessed_letters, word_so_far)
        return False


##########################
####   Display Game   ####
##########################


def display_word_with_guesses(mystery_word, guessed_letters, word_so_far):
    length = len(mystery_word)
    print(('*' * (length * 4 + 4)))
    print(('|' + " " * (length * 4 + 2) + ('|\n')) * 6, end='')
    print('| ', end='')
    print_word(mystery_word, guessed_letters, word_so_far)
    # print("\n\n" + "*" * 30 + "\n\n")
    #mystery_word = mystery_word.split()
    # print(('*' * ((length) * 3) + 4) + '\n\n')


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

    difficulty = select_difficulty()

    mystery_word = get_word_from_file(difficulty)

    tell_how_many_letters(mystery_word, difficulty)

    while True:
        guess = get_user_guess(guessed_letters, guesses_left)
        word_so_far = []
        guessed_letters.append(guess)

        if not check_and_print_match_in_word(mystery_word, guess, guessed_letters, guesses_left, word_so_far):
            guesses_left -= 1

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
