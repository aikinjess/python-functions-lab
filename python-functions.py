# 1

def sum_to(n):
  sum = 0
  i = 0
  while i <= n:
    sum = sum + i
    i+=1
  return sum

# 2

def largest(nums):
    max = 0
    for n in nums:
        if n > max:
            max = n
    return max

print(largest([1, 2, 3, 4, 0]))  # returns 4
print(largest([10, 4, 2, 231, 91, 54]))  # returns 231

# 3

def occurances(string1, string2):
    count = string1.count(string2)
    return count

print(occurances('fleep floop', 'e'))   # returns 2
print(occurances('fleep floop', 'p'))  # returns 2
print(occurances('fleep floop', 'ee'))  # returns 1
print(occurances('fleep floop', 'fe'))  # returns 0

# 4

def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return product 10.0