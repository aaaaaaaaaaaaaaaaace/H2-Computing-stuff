'''
A sorting algorithm that works by picking an element, searches where it is meant to be placed, and inserts it there. 
A loop runs through every element in the array until it becomes sorted.

Time Complexity:
  Worse-case performance: O(n2)
  Best-case performance: O(n)
  Average performance: O(n2)
'''
import random

def InsertionSort(array):
  for i in range(len(array)):
    curr = array[i]
    while i > 0 and curr < array[i - 1]:
      array[i] = array[i - 1]
      i -= 1
     array[i] = curr
  
  return array
 
 
 
# main
arr = [random.randint(1,100) for i in range(10)]
print(arr)
print(InsertionSort(arr))
