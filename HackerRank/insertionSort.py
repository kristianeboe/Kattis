

def insert(array, el):
  for i in range(len(array)):
    array_el = array[i]
    if el < array_el:
      array.insert(i, el)
      return
  array.append(el)

def insertionSort(arr):
  sortedArray = []
  for el in arr:
    insert(sortedArray, el)

 
  return sortedArray


arr2 = [2,1,4,3]
print(insertionSort(arr2))
