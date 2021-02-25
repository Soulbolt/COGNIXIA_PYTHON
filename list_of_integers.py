#Write a function that takes a list of integers and places the zeroes
#in the center of the list. All non-zero integers should keep their
#relative position. Center is defined as floor(length of list / 2).

def centered(list_num):
    list_num.sort()
    print(list_num)

centered(list_num = [1, 1, 3, 0, 6, 0])
centered(list_num = [0, 3, 1])
centered(list_num = [1, 1, 3, 0])
centered(list_num = [1, 1, 3, 0, 6, 0])
    