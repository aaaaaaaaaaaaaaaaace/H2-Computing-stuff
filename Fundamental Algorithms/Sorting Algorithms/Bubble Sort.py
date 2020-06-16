'''
 It iterates by comparing elements pairwise and swapping adjacent elements if they are not in order. 
 The iteration loops itself by how many elements there are in the array, but one less for every consecutive iteration because one more element will be in its correct position for every loop. 
 For an optimised bubble sort, iterating by the number of elements in the array is gratuitous, for the algorithm understands that the array is already sorted, hence will cease its continuation before returning the results, hence it is faster.

Time Complexity:
  Worse-case performance: O(n2)
  Best-case performance: O(n)
  Average performance: O(n2)
  
'''
import random

def BubbleSort(array):
  for i in range(len(array)):
        swapped = False
        for j in range(len(array) - i - 1):
          if array[j + 1] < array[j]:
            array[j],array[j + 1] = array[j + 1],array[j]
            swapped = True
        if not swapped: #OPTIMISATION YOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
          return array
            
  return array
          
              
arr = [random.randint(1,100) for i in range(10)]
print(arr)
print(BubbleSort(arr))
