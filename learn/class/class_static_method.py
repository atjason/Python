
class Date(object):
  
  def __init__(self, day=0, month=0, year=0):
    self.day = day
    self.month = month
    self.year = year
  
  @classmethod
  def from_string(cls, date_as_string):
    day, month, year = map(int, date_as_string.split("-"))
    return cls(day, month, year)

  @staticmethod
  def is_date_valid(date_as_string):
    day, month, year = map(int, date_as_string.split("-"))
    return day <= 31 and month <= 12 and year <= 3999

date_as_string = "24-12-2017"
print Date.is_date_valid(date_as_string)

date = Date.from_string(date_as_string)
print "%d-%d-%d" % (date.day, date.month, date.year)

