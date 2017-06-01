
import time, threading

def loop():
  thread_name = threading.current_thread().name
  print "thread %s started" % thread_name

  for i in range(5):
    print "thread %s >>> %d" % (thread_name, i)
    time.sleep(1)
  
  print "thread %s stopped" % thread_name

print "thread %s started" % threading.current_thread().name

t = threading.Thread(target=loop, name="LoopThread")
t.start()
t.join()

print "thread %s stopped" % threading.current_thread().name

###
balance = 0
lock = threading.Lock()

def change_balance(n):
  global balance
  balance -= n
  balance += n

def run_thread(n):
  for i in range(100):
    lock.acquire()
    try:
      change_balance(n)
    finally:
      lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance

