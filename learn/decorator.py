
import functools

def log(func):
  @functools.wraps(func)
  def wrapper(*args, **kw):
    print "call %s():" % func.__name__
    return func(*args, **kw)
  return wrapper
    
@log
def say_hello():
  print "Hello"

say_hello()
print

###

def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator
    
@log2("execute")
def say_hello2():
  print "Hello2"

say_hello2()
print

def say_hello3():
  print "Hello3"

log2('execute again')(say_hello3)()

