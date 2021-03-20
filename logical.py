#ex1

num1=2
num2=4
num3=8
num4=10
num5=15
print(num1>num2 or num3>num4)
print(num1!=num3 and num4<num5)
print((num4+num5)>0 or num2<num3)
print(not(num2==num4))

#ex2

print(num1>num2 and false)
print(num1>num2 or false)
print((num1>num2) or True)
print(not(num1>num2))


#ex3
bol1,bol2,bol3=True,False,False
bol4=bol1 or bol2 and not(bol3)
print(bol4)
bol5=not(bol1) and bol3 or bol2
print(bol5)
bol6=not(bol2 or bol3)
print(bol6)
bol7=not(bol2 and not(bol3))
print(bol7)
bol8=not(bol1 or bol2) or (bol2 and bol3)
print(bol8)
bol9= bol1 or (bol1 or (bol1 or bol2) or bol3)
print(bol9)
bol10=bol9 and bol2 and not(bol3)
print(bol10)










#ex4
a,b,c,d,e=4,8,3,6,9
bol1=a>b or a>c
print(bol1)
bol2=(a==0.0) or (d==4.9)
print(bol2)
bol3=c<-6 or (d>0 and e==d)
print(bol3)
bol4= ((a+b)>=11) or (d==5)
print(bol4)
bol5=not(a>30 or d<0)
print(bol5)
bol6=not(not(not((a+e)>2 or (c+b)>0) or (e-a)>2))
print(bol6)
bol7=not((b%2)==0)
print(bol7)
bol8=(c%2 > 0 or e%2 > 0 or b%2 > 0) and a%4 == 0
print(bol8)
bol9 = (b//2 > 0 and not(a//2 > 0)) or (not(b//2 > 9) and a//2 > 0)
print(bol9)
bol10 = not (bol3 and (a + b**2 > 50)) or d == e
print(bol10)

