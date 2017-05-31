
from lib.student import Student
  
tom = Student()
tom.score = 60
print tom.score
print tom.score_type

# tom.score_type = "E" # Error: it's read only.
# tom.score = 101      # Error: invalid number.
