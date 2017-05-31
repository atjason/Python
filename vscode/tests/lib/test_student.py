
from demo.lib.student import Student

def test_score():
  tom = Student()
  tom.score = 60
  assert tom.score == 60
  assert tom.score_type == "D"

