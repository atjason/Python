
import functools

int2 = functools.partial(int, base=2)

print int2("111")

###
max2 = functools.partial(max, 10)

print max2(2, 5)

