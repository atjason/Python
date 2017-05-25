# -*- coding: utf8 -*-
"""
有四个数字：1、2、3、4，
能组成多少个互不相同且无重复数字的三位数？各是多少？
"""

result_list = []
nums = [1, 2, 3, 4]

for n1 in nums:
  sub_nums = nums[:]
  sub_nums.remove(n1)

  for n2 in sub_nums:
    sub_sub_nums = sub_nums[:]
    sub_sub_nums.remove(n2)

    for n3 in sub_sub_nums:
      str = "%d%d%d" % (n1, n2, n3)
      result_list.append(int(str))

print result_list

