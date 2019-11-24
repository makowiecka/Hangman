from random import randint

from abstract_word import AbstractWord


class Word(AbstractWord):
    words = ('test',)
    # def __init__(self, random_word: str): # jeśli nie ma konstruktora to jet on wywoływany niejawnie, dzedziczy po klasie object która jest automatycznie wbudowana

    def get_random_word(self) -> str: #dopisujemy self - self mówi szukaj w środku w mojej klasie, w moim obiekcie, dopisuje parametr do funkcji
        word_index = randint(0, len(self.words) - 1)
        return self.words[word_index]

if __name__ == '__main__':
    print(Word().get_random_word())