
def str2int(str):
  def merge_int(x, y):
    return x * 10 + y
  
  def char2int(c):
    char_dict = {
      '0': 0,
      '1': 1,
      '2': 2,
      '3': 3,
      '4': 4,
      '5': 5,
      '6': 6,
      '7': 7,
      '8': 8,
      '9': 9
    }
    return char_dict[c]
  
  # map means apply function to each member in list,
  # and reture a new list.
  int_list = map(char2int, str)

  # reduce means apply function to each memeber with previous result,
  # and return a single result.
  return reduce(merge_int, int_list)

print str2int("423")

###

def format_word(word):
  return word.capitalize()

print map(format_word, ["jason", "APPLE"])
print map(str.capitalize, ["jason", "APPLE"])

###

def plus(x, y):
  return x * y

print reduce(plus, [2, 3, 4])

