name1 : str = 'amna'
name2 : str = "jhon"
name3 : str = "anm"

#list
# * dynamic length
# * hytrigenous data types (Multiple types)
# * Index 
#   *positive o to n-1
#   *negative -1 ti length

#old way
#->         0      1      2
names = ["amna","jhon","anm"] # length-1
#-<       -3      -2    -1
print(names[0])# amna
print(names[-3])# amna
print(names[2])# anm
print(names[1])# jhon
#->         0      1      2
names :list[any] = ["amna","jhon","anm"] # length-1
#-<       -3      -2    -1
print(names[-2])

#for typing import Any
#->         0      1      2
names :list[any] = ["amna","jhon","anm"] # length-1
#-<       -3      -2    -1
print(type(names))
print(type(names[-2]))
print(f'founder of PIAIC {names[-2]. upper()}')

#->         0      1      2
names :list[str] = ["amna","jhon","anm"] # length-1
#-<       -3      -2    -1
print(names[-2])

characters : list[str] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(characters)
#                         0   1   2                                                                                           25
character : list[str] = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#                        -26  -25 -24                                                                                       -3   -2   -1
# default slicing go from left to right
print(character[0:2]) # 0=include : index 2-1=1
print(character[:2]) # not pass any number = all
print(character[-26:-24])# 0=include : index -24-1=-25
print(character[0:2:1]) # 0=include : index 2-1=1
print(character[0:2:]) # 0=include : index 2-1=1

characters : list[str] =  ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
print(characters[::-1])

#                           0   1   2   3   4   5   6   7 
characters : list[str] =  ['A','B','C','D','E','F','G','H']
#                          -8  -7  -6  -5  -4  -3  -2   -1 
# iteration clising ->
# step -> positive
# step -< negative
print(characters[-1:-3:-5])

#List methods
#->         0      1      2
names :list[any] = ["amna","jhon","anm",20,"true"] # length-1
#-<       -3      -2    -1
print(names)

[i for i in dir(list)if"_" not in i]

#->         0      1      2
names :list[any] = ["amna","jhon","anm",20,"true"] # length-1
#-<       -3      -2    -1
print(names)
names[0] =" Amina Amen" #mutable-> editable
print(names)

a : str = print("pakistan") # non_ return function
print(a)

a : str = id (names) # return function
print(a)

# pop method
#->         0      1      2
names :list[any] = ["amna","jhon","anm"] # length-1
#-<       -3      -2    -1
a : str = names.pop() # pop return method
print(a)

names : list[str] =["a","b","c","d","e","f"]
print(names)
names.insert(1 ,"amina")# insert particular position

print(names)
a : list[str]=[1,2,3,4]
a.clear()# remove all elements but object is ramin
print(a)

a : list[str]=[1,2,3,4]
del a  # remove object from memory
print(a)
print(print("pakistan zindabad"))

#->         0      1      2
names :list[any] = ["amna","jhon","anm"] # length-1
#-<       -3      -2    -1
print(names)
a : str = names.pop(0) # pop return method
print(a)
print(names)

# append methods add elements in last
name : list[str]= ["a","b"]
name.append("ameen ullah")# ad element in last
name.append("ameen")# add element in last
name.append("sir zia")# add element in last
print(name)
a : list[str]=['a','b','c','d']
b=a # shallow copy
print(a)
print(b)
b[0]= "pakistan" # change only b variable but both variable updated
print(a)
a : list[str]=['a','b','c','d']
b=a # shallow copy
print(a)
print(b)
b[0]= "pakistan" # change only b variable but both variable updated
print(a)
print(b)
a : list[str]=['a','b','c','d']
b=a.copy() # Deep copy
print("a",a)
print("b",b)
b[0]= "pakistan" # change only b variable but both variable updated
print("a",a)
print("b",b)

# count
names : list[str]= ['a','a','a','b','c','c']
print(names.count("c"))
print(names.count("a"))

names : list[str]=["sir qasim","sir zia"]# GenAI founder members
new_faculty_member : list[str]=['Dr.aman','sir zia']
names.append(new_faculty_member)
names
names : list[str] =["sir zia","muhammad qasim","dr.anam","sir ahsan"]
names.remove("sir zia")# remove with text value
print(names)
names : list[str]= list("ABCDEFG")
print(names)
names.reverse()# in memory = change real data
names
