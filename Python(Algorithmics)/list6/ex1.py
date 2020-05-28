import textdistance
from random_word import RandomWords


class NearestWord:

    def __init__(self, word, hamming_len):
        self.word = word
        self.hamming_len = hamming_len

    def __str__(self):
        return self.word + self.hamming_len


def hamming(text1, text2):
    count_difference = 0
    if len(text1) < len(text2):
        count_difference += len(text2) - len(text1)

    for i in range(len(text1)):
        if i >= len(text2):
            count_difference += len(text1) - len(text2)
            break
        if text1[i] != text2[i]:
            count_difference += 1
    return count_difference


# Return 1 when letter char is near char2(in keyboard)
# Else 0
def near_letters(row, char, char2):
    if char not in row or char2 not in row:
        return 0

    index = row.index(char)

    if row[index - 1] == char2 or row[index + 1] == char2:
        return 1

    return 0


def hamming_include_near_letters(text1, text2):
    keyboard_row1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'w', 'i', 'o', 'p']
    keyboard_row2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
    keyboard_row3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']

    count_difference = hamming(text1, text2)

    for i in range(len(text1)):
        if i >= len(text2):
            break
        if text1[i] != text2[i]:
            count_difference += near_letters(keyboard_row1, text1[i], text2[i]) + \
                                near_letters(keyboard_row2, text1[i], text2[i]) + \
                                near_letters(keyboard_row3, text1[i], text2[i])

    return count_difference


def check_word(dictionary, word):
    if word in dictionary:
        return 'OK'

    hamming_words = []
    for dictionary_word in dictionary:
        hamming_words.append(
            NearestWord(dictionary_word,
                        hamming_include_near_letters(word, dictionary_word)))

    sorted_recommended_words = list(sorted(hamming_words, key=lambda x: x.hamming_len))
    return [sorted_recommended_words[0], sorted_recommended_words[1], sorted_recommended_words[2]]


# ex1 a
distance = hamming('text', 'test')

print("ex1 a")
print(distance)

# ex1 b
distance_near_letters = hamming_include_near_letters('mama', 'nawa')

print("ex1 b")
print(distance_near_letters)

# ex1 c
random_words = RandomWords().get_random_words() + RandomWords().get_random_words()
word = 'dragon'

print('Dictionary', random_words)
print('Similar words' + check_word(random_words, word))
