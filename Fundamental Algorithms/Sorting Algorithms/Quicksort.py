'''
Quicksort is a quick and efficient sorting algorithm. 
It recursively sorts by selecting a pivot and sending all elements smaller than the pivot to the left of it, and the elements larger than it to the right. 
The array is now divided into sub-arrays separated by the pivot picked. The process repeats itself recursively; pivotal exchanges, smaller sub-arrays, until all elements in the prime array are sorted.

Time complexity:
  Worst-case performance:  O(n2)
  Best-case performance: O(n log(n))
  Average performance: O(n log(n))
'''

import random

def Quicksort(array):

  if len(array) <= 1: # base case
    return array 
   
  else:
    left = []
    right = []
    pivot = array[0]
    
    for i in range(1, len(array)):
      if array[i] >= pivot:
        right.append(array[i])
      else:
        left.append(array[i])
        
    return Quicksort(left) + [pivot] + Quicksort(right)
    
    
    
arr = [random.randint(1,100) for i in range(10)]
print(arr)
print(Quicksort(arr))
