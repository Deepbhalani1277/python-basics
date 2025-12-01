name = input("enter your name to print:")

for i in name:
    if(i == "p"):
        print("we have found P")
    else:
        print(i)


colors = ["red", "yellow", "blue"]

for j in colors:
    print(j)
    for h in j:
        print(h)



x = int(input("enter range of numbers:"))

for i in range(x):
       print(i+1)

y=0
while(y<5):
       print(y)
       y = y+1



# Break and continue statment
# break will break the loop when coditon matches
# continue will skip that loop when condition matches

x = int(input("enter the table you want to see:"))

for i in range(1,12):
    if (i == 9):
        continue
    if (i == 11):
        break
    print(x, "x", i, "=", x * i)

