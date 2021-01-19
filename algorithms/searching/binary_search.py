listData = [1,7,10,13,15,22,60,122,156, 174, 177]
value = 7

def binary_search(listData, value):
    low = 0
    high = len(listData) -1 
    while(low <= high):
        # index of middle element round to down
        index_middle = (low+high)//2
        if(listData[index_middle]==value):
            return f'{value} was found and has index {index_middle}'
        elif(listData[index_middle] < value):
            low = index_middle+1
        else:
            high = index_middle-1
    return "Not found"
print(binary_search(listData, value)) #7 was found and has index 1