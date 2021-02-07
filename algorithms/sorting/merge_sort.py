initial_array = [8, 1, 0, 11, 2]

def merge_sort(array):
    if len(array) <= 1:
        return array

    middle = len(array) // 2
    left, right = merge_sort(array[:middle]), merge_sort(array[middle:])
    return merge(left, right)


def merge(left, right):
    output = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1

    output.extend(left[i:]) 
    output.extend(right[j:])

    return output

output = merge_sort(initial_array)
print(output)
