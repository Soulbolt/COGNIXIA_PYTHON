
def area(radius):
    PI = 3.14
    c_area = PI * radius * radius
    
    return  c_area
result = area(4)
print("Area of a circle is : " result)

def volume(c_area, height):
    vol = c_area * height
    return vol

result = volume(50.24, 10)
print("Volume is: " result)