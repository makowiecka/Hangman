
class Easy:
    def __init__(self, chances = 21):
        self.chances = chances

    def get_chances(self):
        return self.chances

    @staticmethod
    def get_name(): #jeśli nie byłoby staticmethod to self
        return 'Easy'

