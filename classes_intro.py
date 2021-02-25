class Car():

    def __init__(self, color, make, year, HP):
        self.color = color
        self.make = make
        self.year = year
        self.HP = HP


    def __gt__(self, other):
        return self.HP > other.HP




my_car = Car("blue", "Ford", 2020, 7)
your_car = Car("red", "Tesla", 2020, 8)

#my_car.start_car()

print(my_car < your_car)
#print(my_car <= your_car)