
import json

d = dict(name="Tom", age=23)

json_str = json.dumps(d)
print json_str

d2 = json.loads(json_str)
print d2 # Note: this string is 'unicode', but not 'str'

###
print

class Student(object):
  def __init__(self, name, age):
    self.name = name
    self.age = age

def student2dict(s):
  # return dict(name=s.name, age=s.age)
  return {
    "name": s.name,
    "age": s.age
  }

def dict2student(d):
  return Student(d["name"], d["age"])

s = Student("Tom", 23)

json_str = json.dumps(s, default=student2dict)
print json_str

json_str = json.dumps(s, default=lambda obj: obj.__dict__)
print json_str

s2 = json.loads(json_str, object_hook=dict2student)
print s2.name

###
print

class Teacher(object):
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  @property
  def json_string(self):
    d = dict(name=self.name, age=self.age)
    return json.dumps(d)

  @staticmethod
  def from_json_string(json_string):
    d = json.loads(json_string)
    return Teacher(d["name"], d["age"])

t = Teacher("Jason", 30)
json_str = t.json_string
print json_str

t2 = Teacher.from_json_string(json_str)
print t2.name

