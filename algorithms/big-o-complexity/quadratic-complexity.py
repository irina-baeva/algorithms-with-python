# quadratic complexity O(n^2)
# example with nested loops

arrayOfTasks = [['cleaning room', 'washing dishes'], ['shopping for grossery', 'shopping for gifts'], ['walking in the park', 'reading']]

n = len(arrayOfTasks) # n = the length of the list here 2

for i in range(0, n): # runs n = 3 times.
    for j in arrayOfTasks[i]: # runs n = 3 times for each value of the i.
        print(j)
