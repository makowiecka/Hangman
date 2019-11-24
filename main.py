from random import randint
from word import Word
from chance import Chance, ChancesError

def get_word_to_guess(word: str) -> list:
    return ['_' for i in word]

def is_word_guessed(letter: str, random_word: str, word_to_guess: list) -> bool:
    if letter not in random_word:
        return False

    index_start = 0
    for i in range(random_word.count(letter)):
        letter_index = random_word.index(letter, index_start)
        index_start = letter_index + 1
        word_to_guess[letter_index] = letter

    return True

def get_letter(random_word) -> str:
    while True:
        letter = input('Podaj literę lub całe słowo: ').lower()

        if letter == random_word:
            win()

        try:
            letter = letter[0]
            break
        except IndexError:
            print('\nTy pacanie, wpisz coś!!!!\n')

    return letter

def win():
    print('Wygrałeś')
    play_again()

def loose(random_word: str):
    print(f'Przegrałeś(aś) :P Szukane słowo to "{random_word}"')
    play_again()

def play_again():
    if 't' == input('Chcesz zagrać ponownie? [t/n] '):
        hangman()

    exit()

def hangman(word: Word, chances): #zmienna word która jest klasy Word
    random_word = word.get_random_word()
    word_to_guess = get_word_to_guess(random_word)

    print('Słowo do odgadnięcia to:')

    while '_' in word_to_guess:
        print(' '.join(word_to_guess))
        print(f'Masz jeszcze {chances.get_chances()} szans')
        letter = get_letter(random_word)
        try:
            if letter in word_to_guess:
                print('Ale to już było... Czytać nie umiesz?')
                chances.decrease()
            if not is_word_guessed(letter, random_word, word_to_guess):
                chances.decrease()
        except ChancesError:
            loose(random_word)

    win()

if __name__ == '__main__':
    hangman(Word(), Chance()) #hangman przyją Word



