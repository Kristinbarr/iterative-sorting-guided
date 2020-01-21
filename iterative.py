import math
from math import sqrt

# O(1) - linear time
def multiply_2(n):
    return n * 2  # multiply step is 1 operation


# O(n) - constant time, n steps: O(n) * O(1) = O(n)
def foo(n):
    for i in range(0, n):  # O(n)
        print(i)  # O(1)

# O(n^2) - n squared: O(1) * O(n) * O(1) * O(n) = O(n^2)
def bar(n):
    s = 0  # O(1)
    for i in range(n):  # O(n)
        for j in range(n):  # O(n)
            s += i * j  # O(1)
    return s

# O() -
def baz(n):
    s = 0  # O(1)
    for i in range(n): # O(n)
        for j in range(int(sqrt(n))):  # O(n^.5)
            s += i * j  # O(1)
    return s

#
def frotz(n):
    s = 0 # O(1)
    for i in range(n): # O(n)
        for j in range(2 * n): # O(n)
			s += j # O(1)
	return s

# O(log) - if steps get divided. n:100000 is 17 steps. O(1) * log(n) = log(n)
def divider(n):
	while n >= 0: # log(n)
		n = n/2 # O(1)

#
def baz(array):
	print(array[1])

	for item in array:
		item = item + 1

	for item in array:
		print(item)
