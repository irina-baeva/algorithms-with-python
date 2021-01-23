'''first step is to create a function to find a smallest number'''

def findSmallest(arr):
    smallest = arr[0] # keep the smallest
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i #changing index of the smallest 
    return smallest_index

print(findSmallest([4, 20, 2, 15])) #2

def selectionSort(arr):
    sortedArray = []
    for i in range(len(arr)):
        smallest = findSmallest(arr) #find the smallest, remove from old array, add to new
        sortedArray.append(arr.pop(smallest))
    return sortedArray


print(selectionSort([4, 20, 2, 15]))#[2, 4, 15, 20]