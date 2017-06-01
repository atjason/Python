
import threading

local_student = threading.local()

def print_name():
  print "Hello %s (in %s)" % \
    (local_student.name, threading.current_thread().name)

def run_thread(name):
  local_student.name = name
  print_name()

t1 = threading.Thread(target=run_thread, args=("Tom",), name="Thread A")
t2 = threading.Thread(target=run_thread, args=("Jason",), name="Thread B")

t1.start()
t2.start()

t1.join()
t2.join()

