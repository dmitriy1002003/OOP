# Класс и методы
class Ship:
    def __init__(self, name: str, capacity: int) -> None:
        self.name = name
        self.capacity = capacity
        self.cargo = 0  # текущий груз, поначалу 0

    def sail(self) -> None:
        print("{} has sailed!".format(self.name))


# Функции
def sail_function(name: str) -> None:
    print("{} has sailed!".format(name))


# Создаем корабль
black_pearl = Ship("Black Pearl", 50)
black_pearl.sail()  # Вывод: Black Pearl has sailed!

# Используем отдельную функцию
sail_function("Flying Dutchman")  # Вывод: Flying Dutchman has sailed!

# Вывод:
# Black Pearl has sailed!
# Flying Dutchman has sailed!
