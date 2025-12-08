'''
# built in functions
# https://www.w3schools.com/python/python_ref_functions.asp

def calgmean(a, b):
    mean=(a*b)/(a+b)
    print(mean)

def isGreater(a, b):
    if(a>b):
        print("first no is greater")
    else:
        print("second no is greater or equal")

def isLeaser(a, b):
    pass 
#if you dont use pass when leaving function blank python compiler will give error 



a = 9
b = 10

isGreater(a, b)
calgmean(a, b)
# gmean = (a*b)/(a+b)
# print(gmean)
'''


#enumerate function
#this function gives index and value both together for current value 


#normal
'''
marks = [20, 56, 40, 50 ,60, 53,11 , 4]
index = 0
for mark in marks:
    print(mark)
    if(index == 3):
        print("deep,awesome!")
    index +=1
'''

#enumerate function
'''

marks = [20, 56, 40, 50 ,60, 53,11 , 4]

for index, mark in enumerate(marks,start = 1):
    print(f"index of {mark} is {index}")
    if (index == 3):
        print("GOOD JOB BOYS")
'''

#lamda function
#lamda function is used to write small functions

'''
cube = lambda x: x*x*x
avg = lambda x, y, z: (x + y + z)/3
print(cube(2))
print(avg(30,30,40))
'''
#map function
#map function applies a function to each element in a sequence and returns new sequence

#syntax map(function, interable)
'''
l1=[1,2,3,4,5,6]
def cube(x):
    return x*x*x

print(cube(2))

# print(type(map(cube,l1)))
newl = (list(map(cube,l1))) 
print(newl)

'''

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# map
squares = list(map(lambda x: x*x, numbers))

# filter
even_squares = list(filter(lambda x: x % 2 == 0, squares))

# reduce 
#reduce function applies a rolling computation to sequential pairs of values in a list 
result = reduce(lambda a, b: a + b, even_squares)

print("Squares:", squares)
print("Even Squares:", even_squares)
print("Sum of Even Squares:", result)
