'''
This sort follows a divide and conquer algorithm. 
The array is first broken up in half repeatedly recursively until every element is by itself.
Two adjacent elements will be compared and put into a temporary array with two sorted elements for all the lone elements. 
The temporary arrays also compare themselves with adjacent arrays and merge correspondingly with their elements sorted as well, until all the elements are in one, single sorted array.

Time complexity:
  Worst-case performance:  O(n log(n))
  Best-case performance: O(n log(n))
  Average performance: O(n log(n))
  
'''
import random

def merge(array1, array2):
    index1 = 0
    index2 = 0
    newarray = []
    
    while index1 < len(array1) and index2 < len(array2):
        if array1[index1] >= array2[index2]:
            newarray.append(array2[index2])
            index2 += 1
        elif array1[index1] < array2[index2]:
            newarray.append(array1[index1])
            index1 += 1
        
    return newarray
    
def MergeSort(array):
  
  if len(array) <= 1: #base case
    return array
   else:
    first = 0 
    last = len(array) - 1
    middle = (first + last) // 2

    return merge(MergeSort(array[:middle]), MergeSort(array[middle:])
    
 
arr = [random.randint(1,100) for i in range(10)]
print(arr)
print(MergeSort(arr))
  
