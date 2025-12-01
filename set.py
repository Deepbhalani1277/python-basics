#set is unordered 
#set do not store duplicate values means when we try to print set which has duplicate values it will print that value only once
'''

s = {2, 2, 56, 5, 8}
print(s)

info = {"deep", 20,True, 5.10,20}

print(info)

deep = set()  #way of creating empty set 
print(type(deep))

'''



#set methods

s1 = {1, 2, 3, 4, 5, 6}
s2 = {3, 6, 7, 8}
#union /update
'''
print(s1.union(s2))  #union doesnt change set 
#update changes the given string or updates...
s1.update(s2)
print(s1, s2)
'''

#intersection/intersection_update
'''
print(s1.intersection(s2))
s1.intersection_update(s2)
print(s1)
'''

#symmetric_difference / symmetric_difference_update
#prints vlaues which are not same in both sets
'''
print(s1.symmetric_difference(s2))
s1.symmetric_difference_update(s2)
print(s1)
'''

#difference / difference update 
#print only which are in s1 but not in s2
'''
print(s1.difference(s2)) #will print value which are in s1 but not in s2
s1.difference_update(s2)
print(s1)
'''


#some other methods
'''
print(s1.isdisjoint(s2))   #if both sets have no common values it will return true else false
print(s1.issubset(s2))     #checks if s1 is subset of s2
print(s1.issuperset(s2))   #checks if s1 is superset of s2

s1.add(9)   #adds value to set
s1.remove(2)  #if value not found it will give error
s1.discard(10)  #if value not found it will not give error
s1.pop()   #removes random value from set as set is unordered
del s2   #deletes entire set
s1.clear()  #removes all values from set

print(s1)
'''

