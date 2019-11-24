# programowanie obiektowe
# musimy stworzyć klase - class - na podstawi eklasy zostanie stworzony obiekt
# obiekt - struktura zamknięta w logiczną całość, jak bedzie działał zależy od nas
# class - na podstawie jednej klasy możemy tworzyć obiekty

class Baton(): # zawsze z dużej litery d
    def __init__(self, sweet: int = 8, nuts: int = 9): # to jest konstruktor nazywamy go dandeint (double under dwa podkreśkenia przed i po), początkowe własności tworzymy w konstruktorze
        self.sweet = sweet # self jeżeli utworzymy obiekt i obiekt bedzie chciał - domyślnie jest ta wartość
        self.nuts = nuts

    def set_sweet(self, sweet): #sety - mam kontrole nad tym co sie dodaje, jakie to są wartości
        self.sweet = sweet

    def get_sweet(self):  # getery zwracają funkcje wartości, dzięk getrom mogę sterować własnościami, my arzucamy ograniczenia
        return self.sweet

snikers = Baton(10, 10) # koniecznie dwa nawiasy bo wywołujemy ukryta funkcje
mars = Baton (nuts=0) # obiket stworzony na podstawie klasy baton
print(Baton().sweet)
print(f' sinkers jest słodki na: {snikers.sweet}')
# snikers.sweet = 10
print(f' sinkers jest słodki na: {snikers.sweet}')
print(f' mars jest słodki na: {mars.sweet}')








