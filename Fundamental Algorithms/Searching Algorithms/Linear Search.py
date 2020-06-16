'''
Just look through every element in an array and check whether it is the target lor.
Nothing too fanciful.

Time complexities:
  Worst-case performance: O(n)
  Best-case performance: O(1)
  Average performance: O(n)
  
'''
import random

def LinearSearch(array, target):
  for i in range(len(array)):
    if array[i] == target:
      return True
  return False
  
  arr = [random.randint(1,100) for i in range(10)]
  target = random.randint(1,100)
  
  print(arr)
  print(target)
  print(LinearSearch(arr, target))
