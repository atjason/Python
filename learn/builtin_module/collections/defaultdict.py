
from collections import defaultdict

dd = defaultdict(lambda: 'Not Found')

dd['key1'] = 'value1'

print dd['key1']
print dd['key2']

