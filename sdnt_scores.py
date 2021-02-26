from operator import itemgetter

student_list = [["Nicholas", 46],["Damon",2],["Naseem",5],["Maria", 89],["Cesar", 5],["Chastity", 5],["John", 17],["Daija", 27],["Jazsmin", 90],["Ken", 23]]

mn = min(student_list, key=itemgetter(1))[1]
temp = []
best = float("inf")
for ele in student_list:
    if mn < ele[1] < best:
        best = ele[1]
        temp = []
        temp.append(ele)
    elif ele[1] == best:
        temp.append(ele)
        second_lowest = sort(temp)
print(temp)