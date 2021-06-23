class Car():
    def __init__(self, *args, **kawargs):
        self.wheels = 4
        self.color = kawargs.get("color", "black")
    def __str__(self):
        return f"It has {self.wheels} wheels and {self.color} color"

porche = Car()
print(porche)

class Convertible(Car):
    def __init__(self, **kawargs):
        super().__init__(**kawargs)
        self.price=40
    

oop = Convertible(color="greem")
print(oop.color)
