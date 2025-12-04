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

marks = [20, 56, 40, 50 ,60, 53,11 , 4]

for index, mark in enumerate(marks,start = 1):
    print(f"index of {mark} is {index}")
    if (index == 3):
        print("GOOD JOB BOYS")