# import os
# import random
# from time import sleep
# import sys
#
#
def cull_list(mystery_word, guess, possible_words, guessed_letters):
    word_dict = {}
    index = 0
    while index < len(mystery_word):
        word_dict[index] = get_position_list(guess, possible_words, index, mystery_word, guessed_letters)
        index += 1

    possible_words = word_dict[max(word_dict.keys(), key=(lambda k: word_dict[k]))]
    print(possible_words[:100], '\n\n^Possible list after cull\n\n\n')
    return possible_words

def get_position_list(guess, possible_words, index, mystery_word, guessed_letters):
    new_list = []
    print(possible_words[:100], '\n^Possible list at start of changing list\n\n\n')

    for word in possible_words:
        if len(word) == len(mystery_word):
            if word[index] == guess and word[index] not in guessed_letters:
                new_list.append(word)
        else:
            continue

    return new_list


def eliminate_other_word_lengths(mystery_word, possible_words):
    for word in possible_words:
        if len(word) != len(mystery_word):
            possible_words.remove(word)
#
    return possible_words
#
#
#
# def clear():
#     if os.name == 'nt':
#         os.system('cls')
#     else:
#         os.system('clear')
#
#
# def print_text(a_string, a_is_slow):
#     if a_is_slow:
#         for words in a_string + "\n":
#             sys.stdout.write(words)
#             sys.stdout.flush()
#             sleep(.04)
#     else:
#         print(a_string)
#
#
# def select_difficulty():
#     difficulty = input("Please select a difficulty:\n\n[E]asy: 4 - 6 characters\n[N]ormal: 6 - 8\n[H]ard:8+ \n>").lower()
#
#     if is_difficulty_valid(difficulty):
#         return difficulty
#     else:
#         print("*" * 40 + "\n")
#         print("Please only type 'e', 'n', or 'h'.\n")
#         print("*" * 40 + '\n')
#         return select_difficulty()
#
# def is_difficulty_valid(difficulty):
#     if difficulty != 'e' and difficulty != 'n' and difficulty != 'h' or len(difficulty) > 1:
#         clear()
#         return False
#     else:
#         return True
#
# # Get word
# def get_word_from_file(difficulty):
#     mystery_word = ''
#     clear()
#     print("*" * 40)
#
#     with open('/usr/share/dict/words', 'r') as f:
#         difficulty_list = get_correct_list(f, difficulty)
#
#         return difficulty_list
#
#
# def get_correct_list(f, difficulty):
#     if difficulty == 'e':
#         difficulty_list = get_easy(f)
#     elif difficulty == 'n':
#         difficulty_list = get_normal(f)
#     elif difficulty == 'h':
#         difficulty_list = get_hard(f)
#
#     return difficulty_list
#
#
# def get_easy(f):
#     easy_list = []
#     for line in f:
#         if 4 <= len(line) <= 6:
#             easy_list.append((line.rstrip()).lower())
#     return easy_list
#
#
# def get_normal(f):
#     normal_list = []
#     for line in f:
#         if 6 <= len(line) <= 8:
#             normal_list.append(line.rstrip())
#     return normal_list
#
#
# def get_hard(f):
#     hard_list = []
#     for line in f:
#         if len(line) >= 8:
#             hard_list.append(line.rstrip())
#     return hard_list
#
#
# def get_user_guess(mystery_word, guessed_letters, guesses_left, word_so_far):
#     print("*" * 40)
#     word_so_far = []
#     guess = input("\nPlease enter your guess. You have {} chances left.\n".format(guesses_left))
#     guess = guess.upper()
#
#     if is_guess_valid(mystery_word, guess, guessed_letters):
#         return guess
#     else:
#         print_word(mystery_word, guessed_letters, word_so_far)
#         return get_user_guess(mystery_word, guessed_letters, guesses_left, word_so_far)
#
#
# def is_guess_valid(mystery_word, guess, guessed_letters):
#     if not is_guess_one_letter(mystery_word, guess, guessed_letters):
#         return False
#     elif not is_guess_a_letter(mystery_word, guess, guessed_letters):
#         return False
#     elif has_been_guessed(mystery_word, guess, guessed_letters):
#         return False
#     else:
#         return True
#
#
# def is_guess_a_letter(mystery_word, guess, guessed_letters):
#     if not guess.isalpha() or guess == '':
#         clear()
#         print("*" * 40)
#         print("\nOnly enter letters. Try again.\n\nThe word is {} letters long.\nSo far, you have guessed: {}\n".format(len(mystery_word), ", ".join(guessed_letters)))
#         return False
#     else:
#         return True
#
# def is_guess_one_letter(mystery_word, guess, guessed_letters):
#     if len(guess) > 1:
#         clear()
#         print("*" * 40)
#         print("\nPlease only guess one letter at a time.\n\nThe word is {} letters long.\nSo far, you have guessed: {}\n".format(len(mystery_word), ", ".join(guessed_letters)))
#         return False
#     else:
#         return True
#
# def has_been_guessed(mystery_word, guess, guessed_letters):
#     if guess in guessed_letters:
#         clear()
#         print("*" * 40)
#         print("\nYou already tried that letter.\n\nThe word is {} letters long.\nSo far, you have guessed: {}\n".format(len(mystery_word), ", ".join(guessed_letters)))
#         return True
#     else:
#         return False
#
#
# def is_match_in_word(mystery_word, guess):
#     if guess in mystery_word:
#         return True
#     else:
#         return False
#
#
# def draw_hangman(incorrect):
#     if incorrect <= 0:
#         print("\n" * 6)
#     else:
#         draw_line_one(incorrect)
#         draw_line_two(incorrect)
#         draw_line_three(incorrect)
#         draw_line_four(incorrect)
#         draw_line_five(incorrect)
#         draw_line_six(incorrect)
#         draw_line_seven(incorrect)
#         draw_line_eight(incorrect)
#     print("*" * 40)
#
#
# def draw_line_one(incorrect):
#     if incorrect > 2:
#         print((" " * 14) + ("_" * 5))
#     else:
#         print('')
#
# def draw_line_two(incorrect):
#     if incorrect > 3:
#         print((" " * 14) + "|" + (" " * 4) + "|")
#     elif incorrect > 1:
#         print((" " * 19) + "|")
#     else:
#         print("")
#
# def draw_line_three(incorrect):
#     if incorrect > 4:
#         print((" " * 14) + "O" + (" " * 4) + "|")
#     elif incorrect > 1:
#         print((" " * 19) + "|")
#     else:
#         print("")
#
# def draw_line_four(incorrect):
#     if incorrect > 6:
#         print((" " * 13) + "/|\\" + (" " * 3) + "|")
#     elif incorrect > 5:
#         print((" " * 14) + "|" + (" " * 4) + "|")
#     elif incorrect > 1:
#         print((" " * 19) + "|")
#     else:
#         print('')
#
# def draw_line_five(incorrect):
#     if incorrect > 5:
#         print((" " * 14) + "|" + (" " * 4) + "|")
#     elif incorrect > 1:
#         print((" " * 19) + "|")
#     else:
#         print('')
#
# def draw_line_six(incorrect):
#     if incorrect > 7:
#         print((" " * 13) + "/ \\" + (" " * 3) + "|")
#     elif incorrect > 1:
#         print((" " * 19) + "|")
#     else:
#         print("")
#
# def draw_line_seven(incorrect):
#     if incorrect > 0:
#         print((" " * 13) + "______|__")
#     else:
#         print('')
#
# def draw_line_eight(incorrect):
#     if incorrect >= 0:
#         print(("_" * 12) + "|_________|" + "_" * 8)
#     else:
#         print("_" * 20 + '\n\n')
#
#
# def display_word_with_guesses(mystery_word, guessed_letters, word_so_far, incorrect):
#     length = len(mystery_word)
#     draw_hangman(incorrect)
#     print('\n')
#     print_word(mystery_word, guessed_letters, word_so_far)
#
#
# def print_word(mystery_word, guessed_letters, word_so_far):
#     if len(mystery_word) == 0:
#         print_text("".join(word_so_far) + '\n', True,)
#         return ''
#
#     for letter in mystery_word:
#         if mystery_word[0] in guessed_letters:
#             word_so_far.append("  " + letter.upper() + "  ")
#             return print_word(mystery_word[1:], guessed_letters, word_so_far)
#         else:
#             word_so_far.append(" __ ")
#             return print_word(mystery_word[1:], guessed_letters, word_so_far)
#
#
# def check_for_win(mystery_word, guessed_letters):
#     number_correct = 0
#
#     for letter in mystery_word:
#         if letter in guessed_letters:
#             number_correct += 1
#         if number_correct == len(mystery_word):
#             return True
#
# def incorrect_guess(mystery_word, guessed_letters, word_so_far, incorrect):
#     clear()
#     draw_hangman(incorrect)
#     print(("\nSorry, that isn't one of the letters. Try again!\n\nSo far, you have guessed: {}\n\n".format(", ".join(guessed_letters))))
#     print_word(mystery_word, guessed_letters, word_so_far)
#
# def correct_guess(mystery_word, guessed_letters, word_so_far, incorrect):
#     clear()
#     draw_hangman(incorrect)
#     print("\nYeah! That one is in there. Keep it up!\n\nSo far, you have guessed: {}\n\n".format(", ".join(guessed_letters)))
#     print_word(mystery_word, guessed_letters, word_so_far)
#
#
# def show_winner(mystery_word, guessed_letters, word_so_far, incorrect):
#     clear()
#     display_word_with_guesses(mystery_word, guessed_letters, word_so_far, incorrect)
#
#     print("\nYOU GOT IT IN {} GUESSES! CONGRATS!\n\n".format(len(guessed_letters)))
#     print("*" * 40 + '\n')
#
# def print_loss_message(mystery_word, word_so_far, incorrect):
#     clear()
#     draw_hangman(incorrect)
#     print("\nSORRY, YOU DIDN'T GET IT THIS TIME.\n\n")
#     print_word(mystery_word, list(mystery_word), word_so_far)
#     print("\n" + "*" * 40 + '\n')
#
#
# def go_again():
#     again = input("\nWould you like to go again? [y/N] \n")
#     if again.lower() == 'y':
#         return True
#
#
# def main():
#     clear()
#
#     guess = ''
#     guessed_letters = []
#     difficulty = 0
#     guesses_left = 8
#     word_so_far = []
#     incorrect = 0
#     possible_words = []
#     difficulty = select_difficulty()
#
#     possible_words = get_word_from_file(difficulty)
#     mystery_word = (random.choice(possible_words).upper())
#     print("First mystery_word: ", mystery_word)
#     print(possible_words[:100], "\n\n\n^ Possible words at start")
#
#
#     print("\nYour word is {} letters long. Good luck!\n".format(len(mystery_word)))
#     print('mystery_word at start: ', mystery_word)
#     while True:
#
#         guess = get_user_guess(mystery_word, guessed_letters, guesses_left, word_so_far)
#         word_so_far = []
#         guessed_letters.append(guess)
#         if not is_match_in_word(mystery_word, guess):
#             incorrect += 1
#             if guesses_left <= 1:
#                 print_loss_message(mystery_word, word_so_far, incorrect)
#                 break
#             incorrect_guess(mystery_word, guessed_letters, word_so_far, incorrect)
#             guesses_left -= 1
#
#         else:
#             if check_for_win(mystery_word, guessed_letters):
#                 clear()
#                 show_winner(mystery_word, guessed_letters, word_so_far, incorrect)
#                 break
#             correct_guess(mystery_word, guessed_letters, word_so_far, incorrect)
#         print("mystery_word before cull: ", mystery_word)
#         # eliminate_other_word_lengths(mystery_word, possible_words)
#         possible_words = cull_list(mystery_word, guess, possible_words, guessed_letters)
#         mystery_word = (random.choice(possible_words).rstrip()).upper()
#         print("mystery_word after cull: ", mystery_word)
#         print(possible_words[:100], "\n\n\npossible words after cull: \n")
#
#
#     if go_again() == True:
#         main()
#
#     clear()
#
# if __name__ == '__main__':
#     main()
