#required arguments
#default arguments
#giving default values like a=10 and b = 5 when def function called default arguments

# def avg(a, b):
#     print("the avg is ", (a+b)/2)
# avg(4, 10)

# def avg1(a=2, b=4):
#     print("the avg is ", (a+b)/2)
# avg1()


def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    # print("average is", sum/len(numbers))
    return ("average is", sum/len(numbers))

c = average(4, 10, 15, 15,20)
print(c)
print(type(c))
