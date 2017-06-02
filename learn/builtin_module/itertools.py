
import itertools

for c in itertools.chain('abc', 'xyz'):
  print c

for key, group in itertools.groupby('aabbbcc'):
  print key, list(group)

