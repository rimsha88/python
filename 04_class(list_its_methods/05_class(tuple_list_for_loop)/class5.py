#List
#iteration operation with loop
#apply any operation on element

names : list[str] = ["amina","anm","amin","jhon"]
print(names)
names : list[str] = ["amina","anm","amin","jhon"]
for name in names:
    print(names)
names =  ["amina","anm","amin"]
i : int =0 #  counter = 0
while i<len(names):# names length =3
 print(names[i])
i += 1
'''
names =names = ["sir zia","sir qqasim","dr.anam"]
for(i =0; names.length; i++){
    names[i]
}
'''

for name in names:
    print(f'welcome dear teacher {name.title()}')

    names : list[str] = ["amina","anm","amin","jhon"]
for name in names:
    print(f'welcome dear teacher {name.title()}')
    print("PIAIC Gen AI TEAM\n")

    names : list[str] = ["amina","anm","amin","jhon"]
for name in names:
    print(f'welcome dear teacher {name.title()}')
    print("PIAIC Gen AI TEAM\n")
    print("pakistan zinda bad")  
names : list[str] = ["amina","anm","amin","jhon"]
for name in names[-2:]:
    print(f'welcome dear teacher {name.title()}')
    print("PIAIC Gen AI TEAM\n")
    print("pakistan zinda bad\n")

data_base : list[tuple[str,str]] =[("sir qasim","123"),
                                   ("sir zia",'345'),
                                   ("sir anam","789")
                                   ]
for row in data_base:
     print(row)


     data_base : list[tuple[str,str]] =[("sir qasim","123"),
                                   ("sir zia",'345'),
                                   ("sir anam","789")
                                   ]
input_user : str = ("enter user name")
input_password : str = ("enter user password")
for row in data_base:
     print(row)
     user,password =row
     if input_user == input_password == password:
        print("valid user")
else:
    print("not found or invalid user name")
    names : list[str] = ["amina","anm","amin","jhon"]
for name in names:
    print(name)

print("hello world")

names : list[str] = ["amina","anm","amin","jhon"]
for name in names:
    print(name)

print("hello world")
names : list[str] = ["amina","anm","amin","jhon"]
for name in names:
    print(name)
    break

print("hello world")

magicians : str = ["alici","david","carolina"]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"i can't wait to see your next trick, {magician.title()}.\n")
    print("thank you everyone ,that was agreat magic show!") # last message for everyone

    #Numbers with loop
#*(range, start, end, step)
range(0)
range(0,10)
list(range(10)) # starting=0 , ending = n-1 , step
list(range(2,21,2)) 

#                     0       1        2
magicians : str = ["alici","david","carolina"]
list(enumerate(magician))
magicians : str = ["alici","david","carolina"]
for index,name in enumerate(magician):
    print(index,name)

    for n in range(1,11):
        print(f"{2} * {n} = {n+2}")