
class _Context(object):
  def __enter__(self):
    print "enter"
  
  def __exit__(self, exctype, excvalue, traceback):
    print "exit"

def connect():
  return _Context()

with connect():
  print "Hello"
  1 / 0 # Note: __exit__ was called even when has exception

