#fstring is for string formatting
 
#this is old way  
'''
letter = "my name is {} and i am from {}  "
letter1 = "my name is {1} and i am from {0}  "
country = "INDIA"
name = "Deep"

print(letter.format(name, country))
print(letter.format(country, name))
print(letter1.format(country, name))

'''
#use of f string methods
'''
print(f"hey my name is {name} and i am from {country}")
print(f"hey my name is {{name}} and i am from {{country}}")
#if we use 2 curly bracket it will not take that as variable but print as it is

'''

#f string is newly introduced from python 3.6 onwards

price = 34.0334
txt = f"for only {price:.2f} dollars!"
#by writing .2f we will get 2 decimal numbers

print(txt)

print(f"{2*30}")
