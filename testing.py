import operator

word_list = ['ECHO', 'HEAL', 'BEST', 'LAZY']
mystery_word = 'break'
guess = 'a'



def cull_list(mystery_word, guess, word_list):
    word_dict = {}
    index = 0

    while index < len(mystery_word):
        word_dict[index] = get_position_list(guess, word_dict, word_list, index)
        index += 1

    word_list = word_dict[max(word_dict.keys(), key=(lambda k: word_dict[k]))]
    return word_list

def get_position_list(guess, word_list, index):
    new_list = []
        for word in word_list:
            if word[index] == guess:
                new_list.append(word)
        return new_list
