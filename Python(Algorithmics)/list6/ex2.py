class LetterFrequencyPercent:
    def __init__(self, letter, frequency):
        self.letter = letter
        self.frequency = frequency


class LetterFrequency:
    def __init__(self, letter, frequency):
        self.letter = letter
        self.frequency = frequency


def check_frequency_letter(alphabet, letters_frequency, text):
    for i in range(len(text)):
        if text[i] in alphabet:
            letters_frequency[alphabet.index(text[i])].frequency += 1
    return letters_frequency


def frequency_letter_to_frequency_letter_percent(letters_frequency):
    sum_letters = 0
    for letter in letters_frequency:
        sum_letters += letter.frequency
    frequency_letter_percent = []
    for letter in letters_frequency:
        frequency_letter_percent.append(LetterFrequencyPercent(letter.letter, letter.frequency / sum_letters * 100))
    return frequency_letter_percent


def check_language(frequency_letter_percent):
    deviation_from_average_polish = 0
    deviation_from_average_dutch = 0
    deviation_from_average_english = 0

    for i in range(len(frequency_letter_percent)):
        deviation_from_average_polish += abs(
            frequency_letter_percent[i].frequency - polish_letters_frequency[i].frequency)

    for i in range(len(frequency_letter_percent)):
        deviation_from_average_dutch += abs(
            frequency_letter_percent[i].frequency - dutch_letters_frequency[i].frequency)

    for i in range(len(frequency_letter_percent)):
        deviation_from_average_english += abs(
            frequency_letter_percent[i].frequency - english_letters_frequency[i].frequency)

    if deviation_from_average_polish < deviation_from_average_dutch and \
            deviation_from_average_polish < deviation_from_average_english:
        return 'It may be polish'

    if deviation_from_average_dutch < deviation_from_average_polish and \
            deviation_from_average_dutch < deviation_from_average_english:
        return 'It may be dutch'

    if deviation_from_average_english < deviation_from_average_polish and \
            deviation_from_average_english < deviation_from_average_dutch:
        return 'It may be english'


# ex2 a
english_letters_frequency = [
    LetterFrequencyPercent('a', 11.68),
    LetterFrequencyPercent('b', 4.434),
    LetterFrequencyPercent('c', 5.238),
    LetterFrequencyPercent('d', 3.174),
    LetterFrequencyPercent('e', 2.799),
    LetterFrequencyPercent('f', 4.027),
    LetterFrequencyPercent('g', 1.642),
    LetterFrequencyPercent('h', 4.200),
    LetterFrequencyPercent('i', 7.294),
    LetterFrequencyPercent('j', 0.511),
    LetterFrequencyPercent('k', 0.856),
    LetterFrequencyPercent('l', 2.415),
    LetterFrequencyPercent('m', 3.826),
    LetterFrequencyPercent('n', 2.284),
    LetterFrequencyPercent('o', 7.631),
    LetterFrequencyPercent('p', 4.319),
    LetterFrequencyPercent('q', 0.222),
    LetterFrequencyPercent('r', 2.826),
    LetterFrequencyPercent('s', 6.686),
    LetterFrequencyPercent('t', 15.97),
    LetterFrequencyPercent('u', 1.183),
    LetterFrequencyPercent('v', 0.824),
    LetterFrequencyPercent('w', 5.497),
    LetterFrequencyPercent('x', 0.045),
    LetterFrequencyPercent('y', 0.763),
    LetterFrequencyPercent('z', 0.045),
]

polish_letters_frequency = [
    LetterFrequencyPercent('a', 10.503 + 0.699),
    LetterFrequencyPercent('b', 1.740),
    LetterFrequencyPercent('c', 3.895 + 0.743),
    LetterFrequencyPercent('d', 3.725),
    LetterFrequencyPercent('e', 7.352 + 1.035),
    LetterFrequencyPercent('f', 0.143),
    LetterFrequencyPercent('g', 1.731),
    LetterFrequencyPercent('h', 1.015),
    LetterFrequencyPercent('i', 8.328),
    LetterFrequencyPercent('j', 1.836),
    LetterFrequencyPercent('k', 2.753),
    LetterFrequencyPercent('l', 2.564 + 2.109),
    LetterFrequencyPercent('m', 2.515),
    LetterFrequencyPercent('n', 6.237 + 0.362),
    LetterFrequencyPercent('o', 6.667 + 1.141),
    LetterFrequencyPercent('p', 2.445),
    LetterFrequencyPercent('q', 0.0),
    LetterFrequencyPercent('r', 5.243),
    LetterFrequencyPercent('s', 5.224 + 0.814),
    LetterFrequencyPercent('t', 2.475),
    LetterFrequencyPercent('u', 2.062),
    LetterFrequencyPercent('v', 0.012),
    LetterFrequencyPercent('w', 5.813),
    LetterFrequencyPercent('x', 0.004),
    LetterFrequencyPercent('y', 3.206),
    LetterFrequencyPercent('z', 4.852 + 0.078 + 0.706),
]

dutch_letters_frequency = [
    LetterFrequencyPercent('a', 7.486),
    LetterFrequencyPercent('b', 1.584),
    LetterFrequencyPercent('c', 1.242),
    LetterFrequencyPercent('d', 5.933),
    LetterFrequencyPercent('e', 18.91),
    LetterFrequencyPercent('f', 0.805),
    LetterFrequencyPercent('g', 3.403),
    LetterFrequencyPercent('h', 2.380),
    LetterFrequencyPercent('i', 6.499),
    LetterFrequencyPercent('j', 1.46),
    LetterFrequencyPercent('k', 2.248),
    LetterFrequencyPercent('l', 3.568),
    LetterFrequencyPercent('m', 2.213),
    LetterFrequencyPercent('n', 10.032),
    LetterFrequencyPercent('o', 6.063),
    LetterFrequencyPercent('p', 1.57),
    LetterFrequencyPercent('q', 0.009),
    LetterFrequencyPercent('r', 6.411),
    LetterFrequencyPercent('s', 3.73),
    LetterFrequencyPercent('t', 6.79),
    LetterFrequencyPercent('u', 1.99),
    LetterFrequencyPercent('v', 2.85),
    LetterFrequencyPercent('w', 1.52),
    LetterFrequencyPercent('x', 0.036),
    LetterFrequencyPercent('y', 0.035),
    LetterFrequencyPercent('z', 1.39),
]

letters_frequency_in_text = [
    LetterFrequency('a', 0),
    LetterFrequency('b', 0),
    LetterFrequency('c', 0),
    LetterFrequency('d', 0),
    LetterFrequency('e', 0),
    LetterFrequency('f', 0),
    LetterFrequency('g', 0),
    LetterFrequency('h', 0),
    LetterFrequency('i', 0),
    LetterFrequency('j', 0),
    LetterFrequency('k', 0),
    LetterFrequency('l', 0),
    LetterFrequency('m', 0),
    LetterFrequency('n', 0),
    LetterFrequency('o', 0),
    LetterFrequency('p', 0),
    LetterFrequency('q', 0),
    LetterFrequency('r', 0),
    LetterFrequency('s', 0),
    LetterFrequency('t', 0),
    LetterFrequency('u', 0),
    LetterFrequency('v', 0),
    LetterFrequency('w', 0),
    LetterFrequency('x', 0),
    LetterFrequency('y', 0),
    LetterFrequency('z', 0),
]

alphabet = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z',
]

# Samogłoski
vowels = [
    'a',
    'e',
    'y',
    'i',
    'o',
    'ą',
    'ę',
    'u',
    'ó',
]

# Spółgłoski
consonants = [
    'b',
    'c',
    'ć',
    'd',
    'f',
    'g',
    'h',
    'j',
    'k',
    'l',
    'm',
    'n',
    'p',
    'r',
    's',
    't',
    'w',
    'y',
    'z',
    'ż',
    'ź',
]

# ex2 b
text = """python - jezyk programowania wysokiego poziomu ogolnego przeznaczenia, o 
rozbudowanym pakiecie bibliotek standardowych, ktorego idea przewodnia jest czytelnosc 
i klarownosc kodu zrodlowego. jego skladnia cechuje sie przejrzystoscia i zwiezloscia.
python wspiera rozne paradygmaty programowania: obiektowy, imperatywny oraz w 
mniejszym stopniu funkcyjny. posiada w pelni dynamiczny system typow i automatyczne 
zarzadzanie pamiecia, bedac w tym podobnym do jezykow perl, ruby, scheme czy tcl. 
podobnie jak inne jezyki dynamiczne jest czesto uzywany jako jezyk skryptowy. 
interpretery pythona sa dostepne na wiele systemow operacyjnych.
python rozwijany jest jako projekt open source zarzadzany przez python software 
foundation, ktora jest organizacja non-profit. standardowa implementacja jezyka 
jest cpython (napisany w c), ale istnieja tez inne, np. jython (napisany w javie), 
clpython napisany w common lisp, ironpython (na platforme .net) i pypy (napisany w pythonie, zob. bootstrap).
"""
frequency_letters = check_frequency_letter(alphabet, letters_frequency_in_text, text)
language = check_language(frequency_letter_to_frequency_letter_percent(frequency_letters))

print("ex2 b")
print(language)

# ex2 c

vowels_in_text = list(filter(lambda x: (x.letter in vowels), frequency_letters))
consonants_in_text = list(filter(lambda x: (x.letter in consonants), frequency_letters))
count_vowels = 0
count_consonants = 0
for vowel in vowels_in_text:
    count_vowels += vowel.frequency
for vowel in consonants_in_text:
    count_consonants += vowel.frequency

print("ex2 c")
print("Count vowels: " + str(count_vowels))
print("Count consonants: " + str(count_consonants))
print("Language by consonants: " + check_language(frequency_letter_to_frequency_letter_percent(
    frequency_letter_to_frequency_letter_percent(frequency_letters))))
print("Language by vowels: " + check_language(frequency_letter_to_frequency_letter_percent(
    frequency_letter_to_frequency_letter_percent(frequency_letters))))