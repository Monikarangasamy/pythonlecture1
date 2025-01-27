 
##Types of scalar objects 
type(7)
<class 'int'>
type(3.0)
<class 'float'>
type(True)
<class 'bool'>
type(False)
<class 'bool'>
type(1234)
<class 'int'>
type(8.99)
<class 'float'>
type(9.0)
<class 'float'>
 
##Type casting
 
float(3)
3.0 
int(5.2)
5
int(5.9)
5
round(5.9)
6 
float(123)
123.0
round(7.9)
8
float(round(7.2))
7.0
int(7.2)
7
int(7.9)
7

##Expressions
print(3+2)
5
print((4+2)*6-1)
30
type((4+2)*6-1)
<class 'int'>
float((4+2)*6-1)
35.0
print((13-4)/(12*12))
0.0625
type(4*3)
<class 'int'>
type(4.0*3)
<class 'float'>
int(1/2)
0
print(5/3)
1.6666666666666667
print(5//3)
1
print(5%3)
2

##python conditions
##(variable=value)
x=6
#6=x :SyntaxError
#x*y = 3+4 :SyntaxError
xy=3+4
xy
7
xy+1
8

pi=355/113
radius=2.2
print(area = pi*(radius*2))
area = pi*(radius*2)
circumference = pi*(radius*2)

##best way
a=355/133*(2.2*2)
c=355/133*(2.2*2)

##meters and feet values execution order
meters =100
feet=3.2802*meters
meters=200
feet
328.02
meters
200

##swapping values
x=1
y=2
y=x
y
1
x=y
x
1
y=2
y=x

x=1
y=2
temp=y
y=x
x=temp
x
2
y
1
