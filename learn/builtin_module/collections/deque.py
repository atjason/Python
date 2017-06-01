
from collections import deque

q = deque(['a', 'b', 'c'])
q.append('d')
q.extend(['e', 'f'])
q.appendleft('x')
print q

q.rotate(1)
print q

