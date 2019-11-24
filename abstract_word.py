from abc import ABC, abstractmethod

class AbstractWord(ABC):

    @abstractmethod #dekoruje jako metoda abstrakcyjna
    def get_random_word(self):
        pass
