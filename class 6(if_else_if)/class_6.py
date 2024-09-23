
# if_else_elif
'''
if_logic:
       True_block
else:
       false_block
'''       
##comprehensive if_else
'''
 True_block if logic else false_block
 '''
 #*if
 #*if_else
 #*if_elif_else

 if True:
      print("pakistan zinda bad")
else:
      print("hello world!")
if False:
    print("pakistan zinda bad")
else:
    print("hello world!")
#        true_block            logic         false_block
print("pakistan zinda bad") if False else("hello world")

if True:
    print("True-block")
elif False:
    print("elif logic1")
elif False:
    print("elif logic2")
elif False:
    print("elif logic3")
else:
    print("final else block")

    #chain1 run only one block
if False:
    print("True-block")
elif True:
    print("elif logic1")
elif True:
    print("elif logic2")
elif True:
    print("elif logic3")
else:
    print("final else block")
print("pakistan")
#chain2 run only one block
if False:
    print("True-block")
elif False:
    print("elif logic1")
elif False:
    print("elif logic2")
elif False:
    print("elif logic3")
else:
    print("final else block")
print("pakistan")

# Grading Rule
from typing import Union
per : Union[int, float] = 88
grade : Union[str, None] = None
if per >= 80:
    grade = "A+"
elif per >= 70:
    grade = "A"
elif per  >= 60:
    grade = "B"
elif per >= 50:
    grade = "C"
elif per >= 40:
    grade = "D"
elif per >= 33:
    grade = "E"
else:
    grade = "Fail"  
print(f"dear student your percentage is {per} now your caluclated grade is:/t  {grade} ")


from typing import Union
per : Union[int, float] = int(input("enter your percentage:/t"))
grade : Union[str, None] = None
if per >= 10:
    grade = "A+"
elif per >= 70:
    grade = "A"
elif per  >= 60:
    grade = "B"
elif per >= 50:
    grade = "C"
elif per >= 40:
    grade = "D"
elif per >= 33:
    grade = "E"
else:
    grade = "Fail"  
print(f"dear student your percentage is {per} now your caluclated grade is:/t  {grade} ")

from typing import Union

try:
    per: Union[int, float] = int(input("Enter your percentage: "))
    grade: Union[str, None] = None
    
    if per >= 90:
        grade = "A+"
    elif per >= 70:
        grade = "A"
    elif per >= 60:
        grade = "B"
    elif per >= 50:
        grade = "C"
    elif per >= 40:
        grade = "D"
    elif per >= 33:
        grade = "E"
    else:
        grade = "Fail"
        
    print(f"Dear student, your percentage is {per}. Your calculated grade is: {grade}.")
except ValueError:
    print("Invalid input! Please enter a valid number.")

    from typing import Union

try:
    per: Union[int, float] = int(input("Enter your percentage: "))
    grade: Union[str, None] = None
    if per >= 10:
        # Add your logic here for when percentage is greater than or equal to 10
        pass
    else:
        # Add your logic here for when percentage is less than 10
        pass
except ValueError:
    print("Invalid input! Please enter a valid number.")