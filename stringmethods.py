#strings are immutable

#string methods create new string 
#by working on old string

a = "deep  !"

print(a.upper())
print(a.lower())


#rstrip method only strip trail part of string 
print(a.rstrip("!"))   


#replace changes all occurences of string with new part
print(a.replace("deep", "Het"))


#split devied the string into list by given chr 
#for example here with space
print(a.split(" "))


# ".capitalize " will convert first chr of string into upper and full string into lower case
blog = "introduction tO pYthon"
print(blog.capitalize())


#center method will center the string as per given parameter
str = "welcome to the charusat"
print(len(str))
print(str.center(50))
print(len(str.center(50)))


#count will count the given para occ in the string
strc = "i am deep, deep is doing great today.!!"
print(strc.count("deep"))


#endswith() it will check if string ends with given para and give boolean output
#we can also check middle part of the string bt giveing starting and ending index with string

print(strc.endswith("!"))
print(strc.endswith("is", 11, 18))

#startswith() true if starts with given sub string
print(strc.startswith("i"))


#find() method is used to find 1st occ of given para from strig
#if this method didnt find any occ of given string it will return -1
print(strc.find("is"))


#index() works same as find() but stops the program with execption when given string is not found in place of -1
print(strc.index("to"))
#it gives error substring not found



#isalnum() method is used to know given string is
#true if made of only A-Z,a-z,0-9
print(strc.isalnum())
isnum = "welcome9"
print(isnum.isalnum())


#isaplha() is same but with out numbers
print(strc.isalpha())
isaplha = "welcome"
print(isaplha.isalpha())


#islower() gives true if  string is in lower case
print(isaplha.islower())

#isupper() true if given string is in upper
print(isaplha.isupper())


#isprintable() give true if all characters in string is printable
ispr = "we wish you a merry christmas\n" #here \n is non printable chr
print(ispr.isprintable())


#isspace() returns true if and only string contains whit spaces
print(ispr.isspace())


#istitle() true if first letter of all words in string are capital
print(ispr.istitle())




#swapcase() converts strings lower to upper and upper to lower
demo = "Hi, I am Deep, what are you doing"
print(demo.swapcase())

#title() converts string into title by capitaliesing all words first chr
print(demo.title())

