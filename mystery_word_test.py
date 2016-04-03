import unittest
from mystery_word import *

guessed_letters = ['a', 'b']

class TestMysteryWord(unittest.TestCase):

    def test_is_difficulty_valid_valid_choices(self):
        self.assertTrue(is_difficulty_valid('e'))
        self.assertTrue(is_difficulty_valid('n'))
        self.assertTrue(is_difficulty_valid('h'))


    def test_is_difficulty_valid_number(self):
        self.assertFalse(is_difficulty_valid(5))


    def test_is_difficulty_valid_multi_letter(self):
        self.assertFalse(is_difficulty_valid('gh'))

    def test_is_difficulty_valid_wrong_letter(self):
        self.assertFalse(is_difficulty_valid('r'))


    def test_is_guess_a_letter_true(self):
        self.assertTrue(is_guess_a_letter('Hello, world.', 'a', guessed_letters))

    def test_is_guess_a_letter_false(self):
        self.assertFalse(is_guess_a_letter('Hello, world.', '7', guessed_letters))


    def test_is_guess_one_letter_False_letter(self):
        self.assertFalse(is_guess_one_letter('Hello, world.', 'df', guessed_letters))

    def test_is_guess_one_letter_int(self):
        self.assertFalse(is_guess_one_letter('Hello, world.', '75', guessed_letters))

    def test_is_guess_one_letter_True(self):
        self.assertTrue(is_guess_one_letter('Hello, world.', 'd', guessed_letters))


    def test_has_been_guessed_False(self):
        self.assertFalse(has_been_guessed('Hello, world.', 'z', guessed_letters))

    def test_has_been_guessed_True(self):
        self.assertTrue(has_been_guessed('Hello, world.', 'a', guessed_letters))


    def test_is_match_in_word_True(self):
        self.assertTrue(is_match_in_word("Hello, world.", "d"))

    def test_is_match_in_word_False(self):
        self.assertFalse(is_match_in_word("Hello, world.", "z"))


    def test_check_for_win_True(self):
        word = "helloworld"
        guessed_letters = ['H', 'E', 'L', 'O', 'W', 'R', 'D']
        self.assertTrue(check_for_win(word.upper(), guessed_letters))

    def test_check_for_win_False(self):
        word = "helloworld"
        guessed_letters = ['E', 'L', 'O', 'W', 'R', 'D']
        self.assertFalse(check_for_win(word.upper(), guessed_letters))





if __name__ == '__main__':
    unittest.main()
# Difficulty selected

# Number of chars output

# User input guess

# Error messages for invalid guesses

# Does guess appear in word

# Does the partial word display (multiple letters guessed)

# Guess count down when incorrect

# Guess count stays when correct

# Game ends on all letters guessed

# game ends on 0 guess count

# word revealed at the end

# play again comes up
