test_case = [1, 2, 3, 4, 6, 8, 11, 18, 20, 22]

def weird_not_weird():
    for num1 in test_case:    
        #num1 = int(input("Please enter number : "))     #ask user for input

        if num1 % 2 != 0:                             #if num1 is odd print Weird
                print("Weird")        
        if num1 in range(2,5):    #num1 within range of 2 - 5
                print("Not weird")                      #if num1 is even and within range of 2 -5 print Not Weird
        if num1 in range(6,20):   #num1 within range of 6-20
                print("Weird")                          #if num1 is even and within range of 6-20 print Weird
        if num1 > 20:            #if num1 is even and greater than 20 print Not Weird
                print("Not Weird")

weird_not_weird()                                   #call Function