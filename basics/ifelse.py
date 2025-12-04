'''
a = int(input("enter you age:"))

print("your age is:", a)

#conditional operators
# >, <, >= , <=, <, ==, !=
print(a>18)
print(a<=18)
print(a==18)
print(a!=18)



if(a> 18):
    print("you can drive")
elif( a == 18):
    print("you can drive")

else:
    print("you can't drive")

'''

    
#short hand if else

a = 300
b = 3303

print("A") if a > b else print("=") if (a==b) else print("B")

c = 9 if a > b else 0
print(c)