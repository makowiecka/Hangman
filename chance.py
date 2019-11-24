class ChancesError(ValueError):
    pass

class Chance():
    def __init__(self, chances: int = 12):
        self.chances = chances

    def get_chances(self): #zwrot ile szans zostało
        return self.chances

    def decrease(self): #pomniejszenie liczby szans
        self.chances -= 1

        if self.chances == 0:
            raise ChancesError('No more chances ')
