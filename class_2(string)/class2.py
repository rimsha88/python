# name : str = "Amina Ameen"
# print(name)
# card : str =f"""  
# PIAIC Student Card
# Student_Name : %s
# father_Name : %s
# age : %d
# education : %s

# """ % (Student_Name, father_Name , education, age)  
# print(card)
# Define the variables
student_name = "Amina Ameen"
father_name = "Ameen"
education = "Bachelor's Degree"
age = 25

# Format the string using the % operator
card = """  
PIAIC Student Card
Student Name : %s
Father's Name : %s
Age : %d
Education : %s

""" % (student_name, father_name, age, education)

# Print the card
print(card)
a: list[str]= [i for i in dir(str) if "_" not in i]
print(a)
print(len(a))