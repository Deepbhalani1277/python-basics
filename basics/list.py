marks = [3,4,5,"deep", True, 14, 15, 132, 1223, "deep12"]

# #list are ordered 
# print(marks)
# print(type(marks))

# #indexing
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])

# #neg-indexing
# print(marks[-3])

# #neg to posi indexing
# print(marks[len(marks)-3])

# #check is element in list
# if 4 in marks:
#     print("yes")
# else:
#     print("no")


# #same things applies for strings as well
# if "eep" in "Deep":
#     print("yes")
# else:
#     print("no")

# print(marks[1:-1])
# print(marks[1:(len(marks)-1)])
# print(marks[1:9:3])


#list comprehension 

# lst = [i*i for i in range(4)]
# print(lst)

# lst1 = [i*i for i in range(10) if i%2==0]
# print(lst1)




#list methods
lsm = [15, 17, 10, 2 , 14, 15]

# lsm.append("hello")

# lsm.sort()

# lsm.sort(reverse=True)

# lsm.reverse()

# print(lsm.index(15))
# print(lsm.count(15))

# m = lsm #copy only refrence 
# m = lsm.copy() #copy values
# m[0] = 0
print(lsm)
# lsm.insert(2, 255)
m = [900, 1000, 1100]
k = lsm + m
print(k)
lsm.extend(m)
print(lsm)