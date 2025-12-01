'''
d1 = {
    "name" : "deep",
    "age" : 18,
    "city" : "anand"
}

print(d1)

print(d1["name"])
print(d1.keys()) #to get all keys
print(d1.values()) #to get all values
print(d1.items()) #to get key value pairs

for item in d1.items():
    print(f"key is {item[0]} and value is {item[1]}")

for key in d1.keys():
    print(f"key is {key} and value is {d1[key]}")
'''


#dictionary methods
ep1 = {122: 45,
      123 : 55,
      124 : 70,
      }
ep2 = {
    222 : 67,
    566 : 90
    }
ep1.update(ep2)
print(ep1)

