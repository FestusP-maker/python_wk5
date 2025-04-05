# Assignment 1: Superhero class with inheritance
class Superhero:
    def __init__(self, name, power, universe):
        self.name = name
        self._power = power
        self.universe = universe

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Power: {self._power}")
        print(f"Universe: {self.universe}")

    def use_power(self):
        print(f"{self.name} uses {self._power}!")

class Villain(Superhero):
    def __init__(self, name, power, universe, evil_plan):
        super().__init__(name, power, universe)
        self.evil_plan = evil_plan

    def use_power(self):
        print(f"{self.name} uses {self._power} for evil!")
        print(f"Plan: {self.evil_plan}")

hero = Superhero("Spider-Man", "Web-Slinging", "Marvel")
villain = Villain("Green Goblin", "Tech Bombs", "Marvel", "Destroy New York")

hero.display_info()
hero.use_power()
print("\n")
villain.display_info()
villain.use_power()


# Activity 2: Polymorphism Challenge
class Vehicle:
    def move(self):
        print("The vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Driving on the road...")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky...")

class Boat(Vehicle):
    def move(self):
        print("Sailing on water...")

vehicles = [Car(), Plane(), Boat()]

print("\nVehicle Movements:")
for v in vehicles:
    v.move()
