'''
A faster but more complex way to search. 
In a sorted array,  the algorithm jumps to the middle element, then compares the target with it. 
If the target is larger than the middle element, the first half of the original array will be neglected, and vice versa.  
This can continue iteratively or recursively for the remaining half of the array, and will continue discarding halves of halves of the array until the middle element is the target.

Time complexity:
  Worst-case performance: O(log(n))
  Best-case performance: O(1)
  Average-case performance: O(log(n))
'''

# Iterative Binary Search

def BinarySearchIterative(array, target):
  first = 0
  last = len(array) - 1
  middle = (first + last) // 2
  
  while last <= first:
    if target == array[middle]:
      return True
      
    elif target <= array[middle]:
      last = middle - 1
    
    else:
      first = middle + 1
  
  return False
  
# Recursive Binary Search
def BinarySearchRecursive(array, target):
  first = 0
  last = len(array) - 1
  
  if last < first:
    return False
  
  else:
    middle = (first + last) // 2
    
    if target == array[middle]:
      retuen True
    elif target > array[middle]:
      BinarySearchRecusrive(array[middle:], target)
    else:
      BinarySearchRecusrive(array[:middle], target)
  
  arr = [random.randint(1,100) for i in range(10)]
  target = random.randint(1,100)
  
  print(arr)
  print(target)
  print(BinarySearchIterative(arr, target)
  print(BinarySearchRecursive(arr, target)
