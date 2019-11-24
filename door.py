class DoorError(RuntimeError): #nowy błąd na podstawie istniejącego, doorerror dziedziczy po Runtimeerror i przyjmuje wszystkie jego własciwości
    pass

class Door: # w klasach tworzymy w liczbach pojedyńczych
    def __init__(self, name: str):
        self.__name = name # ja wstawimy __ - nie mamy dostępu z zewnątrz, jest prywatna z punktu widzenia obiektu
        self.__locked = False
        self.__closed = False

    def open(self):
        if self.__locked:
            raise DoorError('Unlock the door to open them. ')
        self.__closed = False

    def close(self):
        self.__closed = True

    def lock(self):
        if not self.__closed:
            raise DoorError('Close the door to lock them. ')

        self.__locked = True

    def unlock(self):
        self.__locked = False

    def is_locked(self):
        return self.__locked

    def is_closed(self):

        return self.__closed


# print(f'door nazywa się: {__name__}')
if __name__ == '__main__': # name zmienna która przechowuje inf o nazwi modułu. Jeśli uruchamiamy ten moduł bezpośrenia to pod name jest main. Dołączam plik to nazwa pliku

    door = Door('front left')
    try:
        door.close()
        door.lock()
    except DoorError as error_message:
        print(error_message)

    print('qqq', door.is_locked())