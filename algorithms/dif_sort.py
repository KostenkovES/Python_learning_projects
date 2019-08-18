# сортировка пузырьком
def bubbleSort(item):
  for i in range(len(item)):
    for j in range(1, len(item)):
      if item[j-1] > item[j]:
          item[j-1], item[j] = item[j], item[j-1]
  return item

# сортировка выбором
def sortByChoice(item):
  for i in range(len(item)):
    min = i
    for j in range(i+1, len(item)):
      if item[j] < item[min]:
          min = j
    item[min], item[i] = item[i], item[min]
  return item

# сортировка вставками
def sortByInsert(item):
  for i in range(len(item)):
    key = item[i]
    j = i
    while item[j-1] > key and j > 0:
      item[j] = item[j-1]
      j -= 1
    item[j] = key
  return item

# сортировка слиянием
def mergeSort(item):
  if len(item) <= 1:
    return item
  middle = int(len(item)/2)
  left = mergeSort(item[:middle])
  right = mergeSort(item[middle:])
  return merge(left, right)
def merge(left, right):
  result = []
  while len(left) > 0 and len(right) > 0:
    if left[0] < right[0]:
      result.append(left[0])
      left = left[1:]
    else:
      result.append(right[0])
      right = right[1:]
  if len(left):
    result += left
  else:
    result += right
  return result

# быстрая сортировка
def quickSort(item):
  import random
  if len(item) <= 1:
    return item
  else:
    left, middle, right = [], [], []
    rndItem = random.choice(item)
    for element in item:
      if element < rndItem:
        left.append(element)
      elif element > rndItem:
        right.append(element)
      else:
        middle.append(element)
  return quickSort(left) + middle + quickSort(right)

# сортировка кучей
def heapSort(item): 
    for i in range(len(item) , -1, -1):
        heapify(item, len(item), i) 
    for i in range(len(item)-1, 0, -1): 
        item[i], item[0] = item[0], item[i]
        heapify(item, i, 0)
    return item
def heapify(item, n, i): 
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and item[i] < item[left]: 
        largest = left 
    if right < n and item[largest] < item[right]: 
        largest = right 
    if largest != i: 
        item[i],item[largest] = item[largest],item[i]
        heapify(item, n, largest)