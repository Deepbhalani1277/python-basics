import os
'''
# if (os.path.isfile("myfile.text")):
#     f = open("myfile.txt", "r")
#     text = f.read()
#     print(text)
#     f.close()
# else:
#     f.write("hello there")
#     f.append(" general kenobi")
#     print("else block")
      f.close()
# f = open("myfile.txt", "w")
with open("myfile.txt","a") as f:
    f.write("hey i am deep")
'''

#read(),readline(),writeline()

'''
f = open('myfile.txt', 'r') #deafult mode is read 'r'

i = 0
while True:
    i = i + 1 
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(",")[0].replace("(","").replace(")",""))
    m2 = int(line.split(",")[1].replace("(","").replace(")",""))
    m3 = int(line.split(",")[2].replace("(","").replace(")",""))
    print(f"marks of s {i} is: {m1*2}")
    print(f"marks of s {i} is: {m2*2}")
    print(f"marks of s {i} is: {m3*2}")
'''


#file pointer methods: seek(), tell(), truncate()


#seek() and tell() methods
'''
with open("myfile.txt","r") as f:
    f.seek(10)#pointer to 10th byte
    print(f.tell())#current position of pointer
    content = f.read(5)#read 5 bytes from 10th byte
    print(content)
'''

#truncate() method
with open("myfile.txt","w") as f:
    f.write("hello there general kenobi")
    f.truncate(15) #truncate file to 15 bytes  
    
with open("myfile.txt","r") as f:
    content = f.read()
    print(content)
