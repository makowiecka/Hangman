# from word import Word
from abstract_word import AbstractWord
from chance import Chance, ChancesError
from game_level.game_level import GameLevel #pobieram z paczki game level
from words_from_file import WordsFromFile


class Hangman():
    def __init__(self, word: AbstractWord, chance):
        if not isinstance(word, AbstractWord):
            raise ValueError('word needs to be instance of AbstractWord')
        self.random_word = word.get_random_word()   #losowane słowo
        self.chance = chance    # szansa
        self.word_to_guess = ['_' for i in self.random_word]    # słowo do odgadnięcia

    def loose(self):    #przegrywamy
        print('Przegrałeś ')
        self.print_word_to_find()   #drukuje słowo, które było do odgadniecia

    def win(self):  #wygrywamy
        print('Gratulacje !!')
        self.print_word_to_find() #drukjue słowo, które było do odgadnięcia

    def play(self):
        while '_' in self.word_to_guess: #jeślipodkreślenie w słowie do odgadnięcia
            print(' '.join(self.word_to_guess)) #łaczymy
            print(f'Masz jeszcze {self.chance.get_chances()} szans')

            letter = input('Podaj literę lub całe słowo: ').lower()

            if letter == self.random_word: #jeśli litera to całe słowo wygrałeś
                self.win()
                break
            try:
                letter = letter[0] #jeśl kilka liter to pierwszą bierzemy
            except IndexError:     #jeśli nic nie wpisze
                print('\nTy pacanie, wpisz coś!!!!\n')
                continue

            try:
                if letter in self.word_to_guess:    #jeśli powtórzymy litere
                    print('Ale to już było... Czytać nie umiesz?')
                    self.chance.decrease()
                if letter not in self.random_word:  #jeśli nie ma litery pomiejszamy szanse
                    self.chance.decrease()
            except ChancesError: #error w przypadku jak skończą sie wszystkie szanse - przegrales
                self.loose()
                break
            self.append_letter(letter) #zamień literę

        if '_' not in self.word_to_guess: #jeśli nie ma już pustych liter wygrałeś
            self.win()

    def print_word_to_find(self):   #drukujemy szukane słowo to
        print(f'Szukane słowo to: "{self.random_word}"')

    def append_letter(self, letter):    #zamienianie pustego na litere
        index_start = 0
        for i in range(self.random_word.count(letter)):
            letter_index = self.random_word.index(letter, index_start) #index wyszukje
            index_start = letter_index + 1 #startuje od kolejnego, żeby nie powtarzał czynności
            self.word_to_guess[letter_index] = letter #jesli występuje zamieniamy literą

if __name__ == '__main__':
    while 't' == input('Wciśnij "t" aby grać...').lower():
        word = WordsFromFile()
        game_level = GameLevel(Chance)
        chance = game_level.get_level_chances() # tu tworzymym obiekt Game Level bo wnawiasie mamy Chance
        # powyżej chance wywołana funkcja .get_level_chances na obiekcie Game Level
        Hangman(word, chance).play()
