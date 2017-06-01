
from collections import OrderedDict

d = dict(a=1, b=2, c=3)
print d # It's not ordered

od = OrderedDict()
od['c'] = 3
od['a'] = 1
od['b'] = 2
print od # It has same order of insert.

