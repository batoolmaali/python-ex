# a="i hate python"
# print(len(a))


# #strip rstrip lstrip
# a="   i love python    " 

# print(a.strip())

# print(a.rstrip())

# print(a.lstrip())



# b="***love python***" 

# print(b.strip("*"))

# c="*#*love python*#*" 

# # print(c.strip("*#"))


#title
x="i love 2d"
print(x.title())
x="i love 2d"
print(x.capitalize())


# #zfill
# c,b,d= "1" ,"11" , "111"
# print(c.zfill(3))
# print(b.zfill(3))
# print(d.zfill(3))


# #split
# a=" I love python"
# print(a.split())

# a="I-love-python"
# print(a.split("-"))

# c = "I-Love-Python-and-PHP-and-MySQL"
# print(c.split("-", 3))

# d = "I-Love-Python-and-PHP-and-MySQL"
# print(d.rsplit("-", 3))


# # center()

# e = "Osama"
# print(e.center(9))  # Spaces
# print(e.center(9, "#"))  # Hashes
# print(e.center(15, "@"))  # @

# #count
# f = "I Love Python and PHP Because PHP is Easy"
# print(f.count("PHP"))  # 2 PHP Words
# print(f.count("PHP", 0, 25))  # Only One PHP Word


# # swapcase()

# g = "I Love Python"
# h = "i lOVE pYTHON"

# print(g.swapcase())
# print(h.swapcase())


# index(SubString, Start, End)

# a = "I Love Python"
# # print(a.index("P"))  # Index Number 7
# # print(a.index("P", 0, 10))  # Index Number 7
# # print(a.index("P", 0, 5))  # Through Error


# # find(SubString, Start, End)

# b = "I Love Python"
# print(b.find("P"))  # Index Number 7
# print(b.find("P", 0, 10))  # Index Number 7
# print(b.find("P", 0, 5))  # -1



# # rjust(Width, Fill Char) ljust(Width, Fill Char)

# c = "Osama"
# print(c.rjust(10))
# print(c.rjust(10, "#"))

# d = "Osama"
# print(d.ljust(10))
# print(d.ljust(10, "#"))


# e = """First Line
# Second Line
# Third Line"""

# print(e.splitlines())


# # expandtabs()

# g = "Hello\tWorld\tI\tLove\tPython"
# print(g.expandtabs(10))
    

# # one = "I Love Python And 3G"
# # two = "I Love Python And 3g"
# # print(one.istitle())
# # print(two.istitle())

# x = "AaaaaBbbbbb"
# y = "AaaaaBbbbbb111"
# print(x.isalpha())
# print(y.isalpha())

# a = "Hello One Two Three One One"
# print(a.replace("One", "1"))
# print(a.replace("One", "1", 1))
# print(a.replace("One", "1", 2))

# # join(Iterable)

# myList = ["Osama", "Mohamed", "Elsayed"]
# print("-".join(myList))
# print(" ".join(myList))
# print(", ".join(myList))
# print(type(", ".join(myList)))