r = 4
h = 10

def area(radius):
    return(3.14 * radius**2)

def volume(area, height):
    return(area * height)

c_area = area(r)
volume(c_area, h)
print("Area of circle:")
print(c_area)
print("Volume is :")
print(volume(c_area, h))