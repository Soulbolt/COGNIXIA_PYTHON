import math

try:
    import ng_module1
    import ng_module2
except ModuleNotFoundError:
    pass

#print(math.sqrt(4))

color = "blue"
make = "Tesla"
year = 2020
cost = 50


def start_car():
    print("veroom")


def paint_car(new_color):
    color = new_color


print("According to python internals, the name of the file is currently:", __name__)

if __name__ == "__main__":
    print("Im currently on the main module!")
    function1()