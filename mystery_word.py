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
    difficulty = input("Please select a difficulty:\n\n[E]asy: 4 - 6 characters\n[N]ormal: 6 - 8\n[H]ard:8+").lower()

    if difficulty != 'e' or difficulty != 'n' or difficulty != 'h':
        print("Please only type 'e', 'n', or 'h'.\n")
        return select_difficulty

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

    return mystery_word



def get_difficulty_lists():

    with open('/usr/share/dict/words', 'r') as f:
        easy_list = get_easy(f)
        normal_list = get_normal(f)
        hard_list = get_hard(f)

        difficulty_dict = {
        'e':easy_list, 'n':normal_list, 'h':hard_list
        }

    return difficulty_dict



def get_easy(f):
    easy_list = list()

    for line in f:
        if 4 <= len(line) <= 6:
            easy_list.append(line)
    return easy_list


def get_normal(f):
    normal_list = ()

    for line in f:
        if 6 <= len(line) <= 8:
            normal_list.append(line)
    return normal_list


def get_hard(f):
    hard_list = ()

    for line in f:
        if len(line) >= 8:
            get_hard.append(line)
    return get_hard



def tell_how_many_letters(mystery_word):

    print("Your word is {} letters long. Good luck!".format(len(mystery_word)))






#########################
####   Guess Check   ####
#########################



def get_user_guess(guessed_letters):
    guess = input("Please enter your guess. You have {} chances left.\n\nSo far, you have guessed:\n{}\n".format(guesses_left, guessed_letters))

    test_guess(guess, guessed_letters)

    return guess



def test_guess(guess, guessed_letters):
    if len(guess) > 1:
        print("Please only guess one letter at a time.")
        return get_user_guess(guessed)

    has_been_guessed(guess, guessed_letters)


#DONE
def has_been_guessed(guess, guessed_letters):
    if guess in guessed_letters:
        print("You already tried that letter.\n")
        print("So far you have guessed:")
        print(guessed_letters, "\n")
        print(('*' * 20) + '\n\n')
        return get_user_guess()




#################################
####   Checking for Match    ####
#################################


#DONE
def check_and_print_match_in_word(mystery_word, guess, guessed_letters):
    if guess in mystery_word:
        clear()
        print("Yeah! That one is in there. Keep it up!\n\n")
        display_word_with_guesses(mystery_word, guess)
    else:
        clear()
        print("Sorry, that's incorrect.\n\n")
        display_word_with_guesses(mystery_word, guess)
        guesses_left -= 1
        return guesses_left




##########################
####   Display Game   ####
##########################


def display_word_with_guesses(mystery_word, guess):
    mystery_word = mystery_word.split()
    print(((('*' * ((len(mystery_word) * 3)+ 4) + '\n'))) + '*' + ((("' '" * (len(mystery_word + 2)) + '*\n*') * 4)), end='')
    print_word(mystery_word, guess)
    print(('*' * ((len(mystery_word)) * 3) + 4) + '\n\n')



def print_word(mystery_word, guess):
    if len(mystery_word) > 0:
        return print('  *')
    if guess in mystery_word:
        print(" ", guess.upper(), " ", end='')
        print_word(mystery_word[1:], guess)
    else:
        print("___", guess.upper(), " ", end='')
        print_word(mystery_word[1:], guess)



#######################
####   Win Check   ####
#######################


# Not complete
def check_for_win(mystery_word, guessed_letters):
    number_correct = 0

    for letter in mystery_word:
        if letter in guessed_letters:
            number_correct += 1
        else:
            return False

        if len(mystery_word) == number_correct:
            return True



def show_winner(guesses_left):
    print("You got it in {} guesses! Congrats!\n".format(8 - guesses_left))


# Not complete
def print_loss_message(mystery_word, guessed_letters):
    print("Sorry you didn't get it this time.\n\nYou guessed these letters:\n{}\nThe word was ", mystery_word)


####################
####   Again?   ####
####################



# Not complete
def go_again():
    again = input("Would you like to go again? [y/N] \n")
    if again.lower() == 'y':
        True





##################
####   Main   ####
##################


def main():
    clear()

    guess = None
    guessed_letters = []
    difficulty = 0
    random_word = None
    guesses_left = 8

    difficulty = select_difficulty()

    mystery_word = get_word_from_file(difficulty)

    tell_how_many_letters(mystery_word)

    while True:
        get_user_guess(guessed_letters)

        check_and_print_match_in_word(mystery_word, guess, guessed_letters)

        if check_for_win(mystery_word, guessed_letters):
            show_winner(guesses_left)
            break
        elif guesses_left <= 0:
            print_loss_message(mystery_word, guesses_left)

    if go_again() == True:
        main()

    clear()

if __name__ == '__main__':
    main()
