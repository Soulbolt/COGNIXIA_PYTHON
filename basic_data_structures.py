
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8]

list_of_names = ["Kwame", "Cesar", "Jacob"]

a, b, c= list_of_names #"unpacking"
print(a)
#a = list_of_numbers[2:5]
#b = list_of_numbers[5:7]

list_of_numbers.append(10)
print(list_of_numbers)

list_of_numbers[4] = 777

new_list = list_of_numbers.reverse()

print(list_of_numbers)