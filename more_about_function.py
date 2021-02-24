
def some_function(x, y, z):

    final = x + y + z
    return(final)

output = some_function(5, 6, 7)
#print(output)

def greet_friend(name, greeting, sentence):
    output = "{2}, {1}!, {0}".format(greeting, name, sentence)
    return(output)

greet_friend("John", "Hey", "How are you doing today?")
#print(greeting)

def greet_user(greeting):
    user = input("Please enter your name: ")
    print("{}, {}!".format(greeting, user))

greet_user("Hello")