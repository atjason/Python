
class Student(object):

  @property
  def score(self):
    return self._score

  @score.setter
  def score(self, value):
    if not isinstance(value, int):
      raise ValueError("Not a number")
    
    elif value < 0 or value > 100:
      raise ValueError("Score should between [0, 100]")
    
    self._score = value

  @property
  def score_type(self):
    if self._score > 90:
      return "A"
    elif self._score > 80:
      return "B"
    elif self._score > 60:
      return "C"
    else:
      return "D"
  
tom = Student()
tom.score = 60
print tom.score
print tom.score_type

# tom.score_type = "E" # Error: it's read only.
# tom.score = 101      # Error: invalid number.

