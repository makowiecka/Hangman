from door import Door, DoorError # importujemy klase
possible_doors = (
    'front left',
    'front right',
    'rear left',
    'rear right'
)

class Car():
    def __init__(self, doors: int):
        self.doors = {
            possible_doors[i]: Door(possible_doors[i]) for i in range (doors) #dict comprehension, podobnie do list comprehension tylko musi być klucz i wrtość
        }
        self.close_doors()
        #     {
        #     possible_doors[i]: Door(possible_doors[i]) for i in range (doors)
        # }

    def unlock_doors(self):
        for door in self.doors.values():
            door.unlock()

    def lock_doors(self):
        try:
            for door in self.doors.values():
                door.lock()
        except DoorError as message_error:
            print(message_error)

    def close_doors(self):
        for door in self.doors.values():
            door.close()

    def open_doors(self):
        try:
            for door in self.doors.values():
                door.open()
        except DoorError as error_message:
            print(error_message)

    def close_door(self, name):
        try:
            self.doors[name].close()
        except KeyError:
            print(f'There is no such door as "{name}"')

    def open_door(self, name):
        try:
            self.doors[name].open()
        except KeyError:
            print(f'There is no such door as "{name}"')


if __name__ == '__main__':
    maluch = Car(2)

    maluch.unlock_doors()
    maluch.open_doors()

    print('abc', maluch.doors['front left'].is_closed())

