from Vehicle.models import Car, Motorcycle, Truck


car1 = Car("Ford", "jkl", 2010, 4)
motorcycle1 = Motorcycle("Ford", "jkl", 2010, True)
motorcycle2 = Motorcycle("Ford", "jkl", 2010, False)
truck1 = Truck("Ford", "jkl", 2010, 5)
truck2 = Truck("Ford", "jkl", 2010, 15)


def check_number_of_wheels():
    print(111, car1.number_of_wheels())
    print(motorcycle1.number_of_wheels())
    print(motorcycle2.number_of_wheels())
    print(truck1.number_of_wheels())
    print(truck2.number_of_wheels())


check_number_of_wheels()


def unique_properties():
    print(222, car1.number_of_doors)
    print(motorcycle1.has_sidecar)
    print(motorcycle2.has_sidecar)
    print(truck1.load_capacity)
    print(truck2.load_capacity)


unique_properties()


def unique_methods():
    print(333, car1.has_trunk())
    print(motorcycle1.wheelie())
    print(motorcycle2.wheelie())
    print(truck1.is_heavy_load())
    print(truck2.is_heavy_load())
unique_methods()