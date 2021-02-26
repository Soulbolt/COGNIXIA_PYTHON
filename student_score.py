from operator import itemgetter

student_list = [["Nicholas", 46],["Damon",2],["Naseem",16],["Maria", 89],["Cesar", 5],["Chastity", 76],["John", 17],["Daija", 27],["Jazsmin", 90],["Ken", 23]]

# min of all elements
mn = min(student_list, key=itemgetter(1))[1]

# remove elements equal to min
filtered = [x for x in student_list if x[1] != mn]

# get min of remaining
mn_fil = min(filtered,key=itemgetter(1))[1]

# filter remaining
out = [x for x in filtered if x[1] == mn_fil]
print(out)
