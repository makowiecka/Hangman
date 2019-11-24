from chance import Chance
from game_level.abstract_level import AbstractLevel


class GameLevel:
    __levels = (
        {'name':'Easy', 'chances': 21},
        {'name': 'Normal', 'chances': 12},
        {'name': 'Hard', 'chances': 6},
        {'name': 'Super Hard', 'chances': 3}
    )

    def __init__(self, chances):
        self.chances = chances

    def get_level_chances(self):
        for i in range(len(self.__levels)):

            if not isinstance(self.__levels[i], AbstractLevel): # istancja: czy ten obiekt został stworzony z tej klasy
                raise ValueError('Incorect object Instance.') #jeśli nie wyświetli sie error, czyli jęsli level nie został stworzony z klasy AbstractLevel to error

            print('{lp}. {level}'.format(
                  lp=str(i+1),
                level=self.__levels[i]['name'])
            )
        level = int(input('Wybierz poziom trudności'))
        if 0 < level <= len(self.__levels):
            return self.chances(self.__levels[level - 1]['chances'])  # obiekt tworzony na podstawie klasy Chance ale nie będze juz podstawiona wartość 12 tylko przypisze ilość szans w zależności od poziomu trudności

        return self.get_level_chances()

if __name__ == '__main__':
    level = GameLevel(Chance)  # Chance bez nawiasów przekazuje tylko konkretna klase, nie obiekt
    level.get_level_chances()