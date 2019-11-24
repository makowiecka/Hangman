
class Normal:
    def __init__(self, chances=12):
        self.chances = chances

    def get_chances(self):
        return self.chances

    @staticmethod
    def get_name():
        return 'Normal'