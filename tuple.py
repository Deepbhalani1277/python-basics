# tup = (1,3,4,5) #to create single value tuple you have to use comma like (1,) or python will take it as int or given data type
# #tuple is immutable

# print(type(tup),tup)
# # tup[1]=10 #gives error

# if 3 in tup:
#     print("3 in tuple")
# else:
#     print("3 not in tuple")


# print(tup[1:4])
# print(tup)


#operation which can be use on tuple
tup = (2,5,6,23,45,54)


#one way of making changes in tuple is by converting it to list useing list() than making changes using list methods and agian converting it back to tuple 

'''
temp = list(tup)
temp.append("hello")
temp[2] = "world"
newtup = tuple(temp)

print(newtup)

'''

#we can also concat two tuples and create new tuple 

'''

tup1 = (23,434,5465,"dcdvc",435,34)
tup2 = (2323,4,65,"dvc",43,4)

tup3 = tup1 + tup2

print(tup3)

'''


#tuple methods

'''

res = tup.count(2)
res = tup.index(45)
res = tup.index(54)
res = tup.index(45, 2, len(tup)-1)

print(res)

'''

