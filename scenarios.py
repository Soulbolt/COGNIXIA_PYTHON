

def weird_not_weird(num1):
    if num1 % 2 != 0:
        print("Weird")    
    for num1 in range(2,5):
        if num1 % 2 == 0:
            print("weird")
    for num1 in range(6,20):
        if num1 % 2 == 0:
            print("Weird")
        elif num1 % 2 == 0 & num1 < 20:
            print("not Weird")

num1 = input("Please enter number : ")
print(weird_not_weird(num1))