import os
from random import randint

from abstract_word import AbstractWord

class WordsFromFile(AbstractWord):
    @staticmethod #nie będzie działała na żadnych własnosciach danego obiektu
    def get_path(): #ścieżka
        return os.path.abspath(os.path.dirname(__file__))    #biblioteka os, moduł - path, funkcja dirname pierwsza część os.path.abspath - nie musiałoby być kiedyś był bład w programie i lepiej wpisywać

    def get_random_word(self): #zwróci wylosowane słowo tzn wylosuje linie ze zbioru
        words_in_file = self.get_words_count() # odwołujemy się do funkcji poniżej
        word_number = randint(1, words_in_file) #numer losujemy od 1 do całego zbioru
        return self.get_word_from_file(word_number).strip('\n') #zwróci słowo / linie z wylosowanej lini, usówając białe zanki przed i po słowie

    def get_word_from_file (self, word_number): #pobierze konkretne słowo z lini
        with open(f'{self.get_path()}/words.txt', 'r') as file: #otwiera plik
            for i in range(1, word_number + 1):
                word = file.readline()
        return word

    def get_words_count(self): #pobiera informacje o ilości lini czyli słów
        #normlnie pliki zaczytujemy do pamięci i nie martwimy się o nic więcej bo plik nie jest specjalnie wielki
        words_in_file = 0
        with open(f'{self.get_path()}/words.txt', 'r') as file:
            while file.readline():
                words_in_file += 1
        return words_in_file


    # def get_random_word(self) -> str: #dopisujemy self - self mówi szukaj w środku w mojej klasie, w moim obiekcie, dopisuje parametr do funkcji
    #     word_index = randint(0, len(self.words) - 1)
    #     return self.words[word_index]
# if __name__ == '__main__':
#     file = open('words.txt') #poczytać o open
#     while True:
#         line = file.readline()
#
#         if line == '':
#             break
#         print(line.strip()) #funkcja strip usuwa białe znaki z lewej i praej stronie
#
#     file.close() #musimy zamknąc


    #nie musimy pamiętać o zmaykaniu jeśli
# if __name__ == '__main__':

    # with open('words.txt') as file:  # poczytać o open
    #     # python 3.8
    #     #while line := file.readline()
    #     #   print(line.strip())
    #     while True:
    #         line = file.readline()
    #         if line == '':
    #             break
    #         print(line.strip())