# a = "hello world"
# print(a)
# print(type(a))
#
# print(len(a))
# print(a.count("o"))
# print(a.upper())
# print(a.lower())
# print(a.capitalize())
# print(a.index("o"))
# print(a.index("o",0,len(a)-1))
# print(a.casefold()) # opposite of capatilize
# print(a.find("o"))
# name = "john"
# b = "my name is {}"
# print(b.format(name))
# print(name.center(10,"*"))


# *************************** PART 2 *******************************

# a = "hello"
# b = "Hello123"
# c = "123456"
# d = "HELLO"
# e = " "
# f = "Hello 123"
# g = "1.234"

# print(a,a.isalnum())
# print(b,b.isalnum())
# print(c,c.isalnum())
# print(f,f.isalnum()) # counting space as symbol

# print(a,a.isalpha())
# print(b,b.isalpha())
# print(c,c.isalpha())
# print(f,f.isalpha())
#
# print(a,a.isdecimal())
# print(b,b.isdecimal())
# print(c,c.isdecimal())
# print(f,f.isdecimal())
#
#
# print(a,a.isdigit())
# print(b,b.isdigit())
# print(c,c.isdigit())
# print(f,f.isdigit())
#
#
# print(a,a.islower())
# print(b,b.islower())
# print(c,c.islower())
# print(f,f.islower())
#
#
# print(a,a.isupper())
# print(b,b.isupper())
# print(c,c.isupper())
# print(f,f.isupper())
#
#
# print(e,e.isspace())
# print(f,f.isspace())
#
#
# print(a,a.istitle())
# print(b,b.istitle())
# print(c,c.istitle())
# print(f,f.istitle())

# ******************* PART 3 *************************

# a = "harry potter"
# print(a.endswith("t",6,9)) # True

# a = "Harry Potter"
# print(a.startswith("P",6,9))
# print(a.swapcase())


# a = "    Harry Potter    "
# print(a)
# print(a.strip())
# a = "   *****Harry Potter    "
# print(a.strip("*, "))

# a = "OOFD#BRB#OMW#TB"
# print(a.split("#"))

# a = "Harry Potter"
# x = a.ljust(20)
# print(x,"is my favourite movie")
# y = a.rjust(20)
# print(y,"is my favourite movie")

# a = "my name is John"
# print(a.replace("John","Doe"))

a = "Harry potter and the prisoner of azkaban"
print(a.rindex("prisoner"))

