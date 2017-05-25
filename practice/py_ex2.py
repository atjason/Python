# -*- coding: utf8 -*-
"""
斐波那契数列（Fibonacci sequence），又称黄金分割数列。
如：1、1、2、3、5、8
"""

def fibonacci(num):
  result = [1, 1]
  if num <= 2:
    return result[:num]

  a, b = 1, 1
  for i in range(3, num + 1):
    a, b = b, a + b
    result.append(b)

  return result

print fibonacci(0)
print fibonacci(1)
print fibonacci(2)
print fibonacci(3)
print fibonacci(4)
print fibonacci(5)
print fibonacci(6)
print fibonacci(7)

def fibonacci2(num):
  if num < 1:
    return []
  elif num <= 2:
    return 1

  return fibonacci2(num - 2) + fibonacci2(num - 1)

print fibonacci2(0)
print fibonacci2(1)
print fibonacci2(2)
print fibonacci2(3)
print fibonacci2(4)
print fibonacci2(5)
print fibonacci2(6)
print fibonacci2(7)

