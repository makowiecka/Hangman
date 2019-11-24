from game_level.abstract_level import AbstractLevel


class Hard(AbstractLevel):
    # def __init__(self, chances=6):
    #     self.get_chances()

    def get_chances(self):
        return 5

    @staticmethod
    def get_name():
        return 'Hard'