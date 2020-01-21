
# O(1) space complexity
def foo(n):
  total = 0 # O(1)
  for i in range(n): # no complexity
    total += i # no complexity
  return total

# O(1) * O(n) * O(1) = O(n)
def bar(n):
  sums = [] # O(1)
  for i in range(n) # O(n)
  sums.append(i + i) # O(1)


# n squared items for n input. O(1)*O(n)*O(n) = O(n^2)
def baz(n):
  times_table = [] # O(1)

  # O(n) * O(1) = O(n)
  for i in range(n): # O(n)
    row = [] # O(1)

    # O(n) * O(1) = O(n)
    for j in range(n): # O(n)
      row.append(j * i) # O(1)

    times_table.append(row) # row needed to save values

  return times_table
