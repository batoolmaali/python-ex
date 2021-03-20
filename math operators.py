import math
from fractions import *
#ex1
a=15 + 35.6 + 20.78 - 0.01 
print(a)
b=2.0**5 + 100
print(b)

c=2.0**(5+100)
print(c)




#ex2
num1=2
num2=4
num3=6
num4=8
num5=10
num6=12

print(num1<num3)
print(num2<=num6)
print(num3>num4)
print(num5>=num6)
print(num5==num1)
print(num2!=num4)


#ex3
print(math.sqrt(num1))
print(math.sqrt(num4))
print(math.fabs(-num5))
print(math.fabs(-num3))
print(math.fabs(-num3)==math.fabs(-num1))
print(math.sqrt(num6)>math.sqrt(num1))
print(math.sqrt(num6))
print(math.fabs(-num5)<math.fabs(-num2))
print(math.sqrt(math.sqrt(num5)))


#ex4

x=5
y =6*x**2+3*x+2
print(y)

x=.5
y =math.sqrt(math.sqrt(math.sqrt(x/3.6)))
print(y)

a=3
b=10
c=-2 
y=Fraction(-b*(math.sqrt(b**2-4*a*c))(2*a)
print(y)



