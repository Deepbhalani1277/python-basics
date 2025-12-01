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
