array = [123, 1, 0, 31, 20, 23, 25, 226, 221, 4, 7, 8]

def quicksort(array):
    length = len(array)
    if length <= 1: # base case - termination
        return array
    else:
        pivot = array.pop() #take the last one and return
    items_greater = []
    items_lower = []
    for item in array:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return quicksort(items_lower) + [pivot] + quicksort(items_greater) # call the function again


print quicksort(array)  #[0, 1, 4, 7, 8, 20, 23, 25, 31, 123, 221, 226]
