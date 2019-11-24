# possible_doors = (
#     'front left',
#     'front right',
#     'rear left',
#     'rear right'
# )
# class Car():
#     def __init__(self, doors: int):
#         self.doors = {
#             possible_doors[i]: Door(possible_doors[i]) for i in range (doors) #dict comprehension, podobnie do list comprehension tylko musi być klucz i wrtość
#         }
#         self.close_doors()
#         #     {
#         #     possible_doors[i]: Door(possible_doors[i]) for i in range (doors)
#         # }
#
# possible_level = (
#     'easy',
#     'medium',
#     'hard'
# )
# from chance import Chance
# numbe
class Level():
    def __init__(self, easy: int = 16, medium: int = 12, hard: int = 8):
        self.easy = easy
        self.medium = medium
        self.hard = hard

    def get_level(self):
        if choice_level == 'easy':
            return self.easy
        if choice_level == 'medium':
            return self.medium
        if choice_level == 'hard':
            return self.hard

choice_level = input('Wybierz poziom trudności wpisz: easy / medium / hard ').lower()

# class Level():
#     def __init__(self, easy: int = 16, medium: int = 12, hard: int = 8):
#         self.easy = easy
#         self.medium = medium
#         self.hard = hard
#
#     def get_level(self):
#         choice = input('Wybierz poziom trudności wpisz: easy / medium / hard ').lower()
#         if choice == 'easy':
#             return self.easy
#         if choice == 'medium':
#             return self.medium
#         if choice == 'hard':
#             return self.hard




#             print(f'Masz {easy} szans')
# print(Level().easy)

        # #     {
        # #     possible_doors[i]: Door(possible_doors[i]) for i in range (doors)
        # # }
        # def easy(self):
        #     self.chances = 16
        #
        # def medium(self):
        #     self.chances = 12
        #
        # def medium(self):
        #     self.chances = 8