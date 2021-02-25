	#If multiple of 3, print "Fizz"
    #If multiple of 5, print "Buzz"
    #If multiple of both 3 and 5, print "FizzBuzz"

def fibonacci():
    for i in range(1,1000):
        i += 1
        if i % 3 == 0 and i % 5 ==0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 ==0:
            print("Buzz")
        else:
            print(i)

fibonacci()