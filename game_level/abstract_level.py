from abc import ABC, abstractmethod

class AbstractLevel(ABC):

    @abstractmethod #dekoruje jako metoda abstrakcyjna
    def get_chances(self):
        pass

    @staticmethod
    @abstractmethod
    def get_name(self):
        pass

# if __name__ == '__main__':
    # a =AbstrctLevel() # nie można utworzyć obiektu!!