from game_level.levels import Easy, Normal, Hard

class GameLevel:
    __levels = (
        Easy(),
        Normal(),
        Hard()
    )

    def __init__(self, chances_name):    # tworzymy obiekt
        self.chances_name = chances_name

    def get_level_chances(self):
        for i in range(len(self.__levels)):
            print('{lp}. {level}'.format(
                lp=str(i+1),
                level = self.__levels[i].get_name())
            )

        level = int(input('Wybierz poziom trudności'))
        if 0 < level <= len(self.__levels):
            chance_object = self.chances_name(self.__levels[level - 1].get_chances()) #stworzony obiekt
            return chance_object

        return self.get_level_chances()

# klasa abstarkcyjna - klasa po której można dziedziczyc ale nie można tworzyć obiektów
# musimy rozróżniać gdzie tworzymy nowy obiekt