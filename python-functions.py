# P. 1

from math import prod


def sum_to(n):
  sum = 0
  for num in range(1, n+1):
    sum += num
  print(sum)

sum_to(6)
sum_to(10)

# P. 2

def largest(list):
  return max(list)

print(largest([10, 4, 2, 231, 91, 54]))

# P. 3

def occurences(str1, str2):
  return str1.count(str2)

print(occurences('fleep floop', 'e'))
print(occurences('fleep floop', 'floop'))

# P. 4

def product(*args):
  product = 1
  for x in args:
    product *= x
  return product

print(product(-1, 4)) # returns -4
print(product(2, 5, 5)) # returns 50
print(product(4, 0.5, 5)) # returns 10.0