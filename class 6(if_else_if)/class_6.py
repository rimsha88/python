
from typing import Union
per : Union[int, float] = 88
grade : Union[str, None] = 
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
print(f"dear student your percentage is {per} now your caluclated grade is:/t {grade}")


