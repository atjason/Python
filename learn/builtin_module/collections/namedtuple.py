
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

p = Point(1, 2)
print "(%d, %d)" % (p.x, p.y)

