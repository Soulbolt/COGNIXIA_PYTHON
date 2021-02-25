import math

class Calculator():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):        
        return self.x + self.y

    def sub(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        
        if (y == 0 or x == 0):
            a = "You can't divide vy zero."
        else:
            return self.x / self.y      

    def sqrt(self):
        return math.sqrt(x), math.sqrt(y)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

obj = Calculator(x, y)
while True:
    
    def menu():
        b = ('1. Add \n2. Sub \n3. Multiply \n4. Divide \n5. SquareRoot \n-1. To Quit') 
        print(b)
    menu()
    choice = int(input('Please select one of the options above : ')) 
    if choice == 1:
        print("Result: ",obj.add())
    elif choice == 2:
        print("Result: ",obj.sub())
    elif choice == 3:
        print("Result: ",obj.multiply())    
    elif choice == 4:
        print("Result: ",obj.divide())
    elif choice == 5:
        print("Result: ",obj.sqrt())
    elif choice == 0:
        print('Again try one of the following')
    elif choice == -1:
        print('You have exited the Calculator.')
        break
    else:
        print('Invalid option') 
        break       
print()