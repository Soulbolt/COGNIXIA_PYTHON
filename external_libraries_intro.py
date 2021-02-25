import math

try:
    import ng_module1
    import ng_module2
except ModuleNotFoundError:
    pass

#print(math.sqrt(4))

PI = math.pi
E = math.e

#print(dir(math))
def function1():
    pass


def function2():
    pass


print("According to python internals, the name of the file is currently:", __name__)

if __name__ == "__main__":
    print("Im currently on the main module!")
    function1()