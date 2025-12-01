import time

# time1 = time.strftime("%H")
# curr = int(time1)
# print(time1)
curr = int(input("enter hour:"))

if(curr >= 0 and curr < 12):
    print("Hello sir, Good Morning.")
elif(curr >=12 and curr < 17):
    print("Hello sir, Good Afternoon.")
else:
    print("Hello sir, Good Night.") 
