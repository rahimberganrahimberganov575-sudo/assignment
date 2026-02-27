class Warehouse:
    def __init__(self, name, total_capacity, stored_crates=0):
        self._name = name
        self.total_capacity = total_capacity
        self.stored_crates = stored_crates

    @property
    def total_capacity(self):
        return self._total_capacity

    @total_capacity.setter
    def total_capacity(self, value):
        if value < 1:
            raise ValueError("Total capacity must be at least 1")
        self._total_capacity = value

    @property
    def name(self):
        return self._name

    def ship(self, crates):
        if crates < 0:
            raise ValueError("Number of crates must be positive")
        elif self.stored_crates - crates < 0:
            raise ValueError("Cannot ship more than stored")
        else:
            self.stored_crates -= crates

    def store(self, crates):
        if crates < 0:
            raise ValueError("Number of crates must be positive")
        elif self.stored_crates + crates > self.total_capacity:
            raise ValueError("Not enough free space")
        else:
            self.stored_crates += crates

    @property
    def stored_crates(self):
        return self._stored_crates

    @stored_crates.setter
    def stored_crates(self, value):
        if value < 0:
            raise ValueError("Stored crates cannot be negative")
        elif value > self.total_capacity:
            raise ValueError("Stored crates cannot exceed total capacity")
        self._stored_crates = value

    @property
    def usage_rate(self):
        return round((self.stored_crates / self.total_capacity) * 100, 1)

    @property
    def free_space(self):
        return self.total_capacity - self.stored_crates

w = Warehouse("East", 500)
print(w.name, w.free_space, w.usage_rate)
w.store(350)
print(w.stored_crates, w.usage_rate)
w.ship(100)
print(w.free_space)

try:
    w.store(300)
except ValueError as e:
    print(e)

try:
    w.name = "X"
except AttributeError:
    print("Cannot change warehouse name")
