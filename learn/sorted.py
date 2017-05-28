
num_list = [3, 5, 2, 6, 1]

print sorted(num_list)

###

def reserve_cmp(x, y):
  return -cmp(x, y)

print sorted(num_list, reserve_cmp)

###

str_list = ['bob', 'about', 'Zoo', 'Credit']

print sorted(str_list)

###

def cmp_ignore_case(str1, str2):
  return cmp(str1.lower(), str2.lower())

print sorted(str_list, cmp_ignore_case)

