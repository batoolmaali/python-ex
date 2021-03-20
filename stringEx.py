#ex1
#1
x="Triceratops"
print(x.upper())
#2
c="Triceratops"
print(c.lower())
#3
f ="Triceratops"
print(f.count("t"))
#4
b = "Triceratops"
print(b.find("p")) 
#5
b = "Triceratops"
print(b.find("a")) 
b = "Triceratops"
print(b.index("a")) 


#ex2

name = "ayham zaid"
country = "The Kingdom of Jordan"

print(" {:s} {:s}".format(name,country))


#ex3
s="'joijfowijvroijvojq'"
a= "a"
i="i"
e="e"
o="o"
u="u"
print(s.count("i"))
print(s.count("a"))
print(s.count("e"))
print(s.count("o"))
print(s.count("u"))

print(" {:s} {:d}".format(a,s.count("a")))
print(" {:s} {:d}".format(i,s.count("i")))
print(" {:s} {:d}".format(e,s.count("e")))
print(" {:s} {:d}".format(u,s.count("u")))
print(" {:s} {:d}".format(o,s.count("o")))

#ex4
firstname="batool"
lastname="maali"

#slicing
#[start:end] end not include
#[start:end:steps]

print(firstname[0:1]+lastname[0:1])

#ex5
string="Allosaurus"
print(string[0:4])
print(string[3:7])
print(string[6:])
print(string[2:])
print(string[8:])

#ex6
a="i hate python"
print(len(a))

#ex7

a = "jordan"
print("b" in (a)) 
a = "Amman"
print("a" in ("Amman")) 
a = "Egypt"
print("t" in (a)) 

# a="Khuraibet  Al-Souq"
# print(' ' in (a)) 


# b="love python***" 

# print(b.strip("x"))


#ex9
name = "ayham zaid"


print(" {:s}[AZ]".format(name))

#EX10

Y= "Orange"
print(Y[0:2]+Y[4:])

X="ME"
print(X*2)

#ex11

w="Ayham"
print(w[1:])
print(w[0:1]+w[2:])
print(w[0:3]+w[4:])

e="batool"
print("".join(reversed(e)))


#ex12
a,b,c,d,e,f= "cow","pig","horse","goat","dog","cat"
a1,b1,c1,d1,e1,f1= 50,30,3,3,2,3

print("there are {:d}{:s},{:d}{:s},{:d}{:s},{:d}{:s},{:d}{:s},{:d}{:s} on the farm".format(a1,a,b1,b,c1,c,d1,d,e1,e,f1,f))