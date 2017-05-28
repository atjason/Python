
def is_odd(n):
  return n % 2 == 1

print filter(is_odd, range(10))

###

def not_empty(str):
  return str.strip()

print filter(not_empty, ["Hello", " ", "Python."])

