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
