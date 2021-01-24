unsorted_list = [2,6,5,4,3,7,8]

def bubbleSort(list_a):
    indexing_length = len(list_a) - 1
    sorted = False        #flag to check if array sorted
    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            # print(list_a)
            if list_a[i] > list_a[i+1]: #check 2 numbers
                sorted = False # when we have sorted items, this flag will not be activated and it will break the loop 
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i] #flip
    return list_a
        
'''
steps:
[2, 6, 5, 4, 3, 7, 8]
[2, 6, 5, 4, 3, 7, 8]
[2, 5, 6, 4, 3, 7, 8]
[2, 5, 4, 6, 3, 7, 8]
[2, 5, 4, 3, 6, 7, 8]
[2, 5, 4, 3, 6, 7, 8]
[2, 5, 4, 3, 6, 7, 8]
[2, 5, 4, 3, 6, 7, 8]
[2, 4, 5, 3, 6, 7, 8]
[2, 4, 3, 5, 6, 7, 8]
[2, 4, 3, 5, 6, 7, 8]
[2, 4, 3, 5, 6, 7, 8]
[2, 4, 3, 5, 6, 7, 8]
[2, 4, 3, 5, 6, 7, 8]
[2, 3, 4, 5, 6, 7, 8]
[2, 3, 4, 5, 6, 7, 8]
[2, 3, 4, 5, 6, 7, 8]
[2, 3, 4, 5, 6, 7, 8]
[2, 3, 4, 5, 6, 7, 8]
[2, 3, 4, 5, 6, 7, 8]
[2, 3, 4, 5, 6, 7, 8]
[2, 3, 4, 5, 6, 7, 8]
[2, 3, 4, 5, 6, 7, 8]
[2, 3, 4, 5, 6, 7, 8]
[2, 3, 4, 5, 6, 7, 8]
'''
print(bubbleSort(unsorted_list))