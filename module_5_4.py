class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        new_object = object.__new__(cls)
        cls.houses_history.append(args[0])
        return new_object

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        elif new_floor == self.number_of_floors:
            print('Вы на нужном этаже')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name},количество этажей: {self.number_of_floors}')

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other

    def __ne__(self, other):
        return not self.__eq__

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other

    def __le__(self, other):
        return not self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors > other

    def __ge__(self, other):
        return not self.__gt__(other) or self.__eq__(other)

    def __add__(self, value):
        if isinstance(value, House):
            self.number_of_floors += value.number_of_floors
        elif isinstance(value, int):
            self.number_of_floors += value
        return self

    def __iadd__(self, value):
        return self.__add__(value)

    def __radd__(self, value):
        return self.__add__(value)
    def __del__(self):
        print(f'{self.name} снесен, но он останется в истории')


h1 = House('ЖК Горский', 18)
print(House.houses_history)
h2 = House('Домик в деревне', 2)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
del h2
del h3

print(House.houses_history)
