class Ship:
    def __init__(self, name: str, capacity: int) -> None:
        self.name = name
        self.capacity = capacity
        self.cargo = 0  # начальный груз - 0

    def load_cargo(self, weight: int) -> None:
        if self.cargo + weight <= self.capacity:
            self.cargo += weight
            print("Loaded {} tons".format(weight))
        else:
            print("Cannot load that much")

    def unload_cargo(self, weight: int) -> None:
        if self.cargo - weight >= 0:
            self.cargo -= weight
            print("Unloaded {} tons".format(weight))
        else:
            print("Cannot unload that much")


# Создаем корабль грузоподъемностью 100
ship = Ship("Black Pearl", 100)

# Пробуем загрузить 50 
ship.load_cargo(50)  # Вывод: Loaded 50 tons

# Пробуем загрузить еще 60
ship.load_cargo(60)  # Вывод: Cannot load that much

# Разгружаем 30
ship.unload_cargo(30)  # Вывод: Unloaded 30 tons

# Пробуем разгрузить больше, чем уже есть на борту
ship.unload_cargo(30)  # Вывод: Cannot unload that much
