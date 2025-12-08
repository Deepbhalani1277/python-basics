print("hello world")
print("7+34")
print (10+12)
print("bye")

#single and multiline comments

#escape sequence

st = '''

hello

print("hello\n\"world\" ")


a=1
print(a)
deep = 10
b= deep
c="Deep"
print(b,"\n",c)

print(a+b)
print(type(a))

'''







a = "1"
b = "2"

print(int(a)+int(b))

#implicite type casting
c = 1.9
d = 8
print(c+d)


#user input

a = input("enter your name:")
print("my name is deep",a)

c = int(input("enter number 1:"))
D = int(input("enter number 2:"))

print("sum of both is", c + D )


#string

name = "deep"
friend = "Het"
anotherfriend = "Heer"
print(name[0])
print("my name is:", name )



#loop through the string


for cha in name:
    print(cha)


#paragraph in string

para = '''
hi my name is deep
i am 18 years old
'''

# print(st)

'''
print("")

print(para)
'''

#string slicing 
'''
print(len(name))
print(name[0:3])
print(name[0:-3]) #if you write -3 it will take length of string than - that index from string

harry = "harry"
print(harry[-4:-1])

'''


#difference between "is" and "=="   

#"is" compares memory location 
#and
# "==" compares values

'''
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)   # True
print(a is b)   # False
'''

'''
a = b = [1, 2, 3]
print(a is b)   # True
print(a == b)   # True
'''