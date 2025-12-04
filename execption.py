#single Exception handling
'''
a = input("enter a number:")

print(f"multiplication table of {a} is:")

try:
    for i in range (1, 11):
        print(f"{int(a)} X {i} = {int(a)* i}")
except Exception as e:
    print("desorry some error occurred")
    print(e)
print("some imp lines of code")
print("end of program")

'''

#multiple exception handling
'''
try:
    num = int(input("enter a number:"))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("entered number is not integer")
except IndexError:
    print("please enter valid index")



#finally

finally:
    print("finally always gets executed no matter exeception is found or not")

'''

#custome execeptions
#we can use raise keyword to customely call any errors

a = int(input("enter and value between 5 and 9:"))

if(a<5 or a>9):
    raise ValueError("value should be between 5 and 9")

