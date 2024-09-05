class Vehicle:
    def __init__(self, make, model, year):
        self.make = make  # Manufacturer of the vehicle (e.g., Toyota)
        self.model = model  # Model of the vehicle (e.g., Camry)
        self.year = year  # Year of manufacture

    def number_of_wheels(self):
        raise NotImplementedError("Subclasses must implement this method")


class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.number_of_doors = doors

    def number_of_wheels(self):
        return 4

    def has_trunk(self):
        return True


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, sidecar):
        super().__init__(make, model, year)
        self.has_sidecar = sidecar

    def number_of_wheels(self):
        if self.has_sidecar == True:
            return 3
        else:
            return 2

    def wheelie(self):
        if self.has_sidecar == True:
            return "no"
        else:
            return "yes"


class Truck(Vehicle):
    def __init__(self, make, model, year, capacity):
        super().__init__(make, model, year)
        self.load_capacity = capacity

    def number_of_wheels(self):
        return 18

    def is_heavy_load(self):
        if self.load_capacity > 10:
            return True
        else:
            return False
