
word_list = (ATM, CV, SUV, TV)

class WordFromFile():
    def __init__(self, words: str):
        pass

class Car():
    def __init__(self, doors: int):
        self.doors = {
            possible_doors[i]: Door(possible_doors[i]) for i in range (doors) #dict comprehension, podobnie do list comprehension tylko musi być klucz i wrtość
        }
        self.close_doors()