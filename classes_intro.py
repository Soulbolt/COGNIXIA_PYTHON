class Car():

    wheels = 4
    doors = True

    def __init__(self, color, make, year, HP):
        self.color = color
        self.make = make
        self.year = year
        self.HP = HP


    def __gt__(self, other):
        return self.HP > other.HP

    def __str__(self):
        return self.make




my_car = Car("blue", "Ford", 2020, 150)
your_car = Car("red", "Tesla", 2020, 200)

#my_car.start_car()

print(my_car < your_car)
#print(my_car <= your_car)