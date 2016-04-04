import unittest
from mystery_word_normal_final import *

guessed_letters = ['a', 'b']

class TestMysteryWord(unittest.TestCase):

### USER ENTERS 'E' ###
    def test_is_select_difficulty(self):
        self.assertEqual(select_difficulty(), 'e')


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



    ### USER ENTERS 'a' ###
    def test_get_user_guess(self):
        self.assertEqual(get_user_guess('apple', [guessed_letters], '8', ['a']), 'A')


    def test_is_guess_a_letter_true(self):
        self.assertTrue(is_guess_a_letter('Hello, world.', 'a', guessed_letters))

    def test_is_guess_a_letter_false(self):
        self.assertFalse(is_guess_a_letter('Hello, world.', '7', guessed_letters))


    def test_is_guess_one_letter_False_letter(self):
        self.assertFalse(is_guess_one_letter('Hello, world.', 'df', guessed_letters))

    def test_is_guess_one_letter_False_int(self):
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


### USER ENTERS 'y' ###
    def test_go_again(self):
        self.assertTrue(go_again(), )



if __name__ == '__main__':
    unittest.main()
