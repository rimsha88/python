# Python divides the operators in the following groups:

# *Arithmetic operators
# *Assignment operators
# *Comparison operators
# *Logical operators
# *Identity operators
# *Membership operators
# *Bitwise operators
#!conda install lxml -y


#python Airthmetic operators
# !pip install pandas
# import pandas as pd
#table = pd.read_html('https://www.w3schools.com/python/python_operators.asp')
#table[0]


a : int = 7
b : int = 6
print(a+b)  #addition
print(a-b)  #subtraction
print(a*b)  #multiplication
print(a%b)   #module
print(a/b)   #division

a : int = 5
b : int = 8
print(a%8)   

a : int = 88
b : int =96
print(a//b)
print(a/b)

print(14.7/6)

#python assignment operator

# +=
a : int = 5
print(a)
a : int = a + 3
print(a)

# -=
a : int = 5
print(a)
a -=4
print(a)

# *=
a : int = 5
print(a)
a *=4
print(a)

# %=
a : int = 6
print(a)
a %=7
print(a)

# //=
a : int = 6
print(a)
a //=7
print(a)

# **=
a : int = 6
print(a)
a **=7
print(a)


a : int = 7
print(b :=a)

#Python Comparison Operators
a : int = 7
b : int = 7
print(a==b)
# a==b
# 7==10
#true
# ==
a : int = 7
b : str = '7'
print(a==b)
# a==b
# 7==10
#true

# !=
a : int = 7
b : str = 8
print(a!=b)

# >=
a : int = 7
b : str = 8
print(a>=b)

# <=
a : int = 7
b : str = 8
print(a<=b)

# >
a : int = 7
b : str = 8
print(a>b)
# <
a : int = 7
b : str = 8
print(a<b)


#Python Logical Operators
name : str = "Amina Ameen"
print(not name== "Amina Ameen")
# name== 'Amina Ameen' 
#"Amina== Ameen"

# python identity operators
x : str = "abc"
z : str = "abc"
print(id(x))
print(id(z))

#python membership operators
names :list[str] = [chr(i) for i in range(65,91)]
for i in range(len(names)):
    print(i, names[i])


names : list[str] = ["sir","maam","student"]
uinput : str =input ("enter your name")
uinput is not names

names : list[str] = ["sir","maam","student"]
uinput : str =input ("enter your name")
uinput is names

#PEMDAS
print(3+2-2*4/2+2)
#     3+2-8/2+2
#     3+2-4+2
#    6     -8

print((6+2)-((3+7)))

universe_age :int = 14_000_000_000
print(universe_age)

import cgi
#
#0  1   2      0     1    2
a , b , c = "amina","7","8.9"
print(a)
print(b)
print(c)
a , b , c = ("amina","7","8.9")
print(a)
print(b)
print(c)

data : str = ("amna",5,8.9)
print(data[0],data[1],data[2])

data : str = ("amna",5,8.9)
print(*data)