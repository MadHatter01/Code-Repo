#time complexity = c(n) * levels of the tree = c(n) * (log2n + 1) = theta(nlogn)

def merge(left, right):
    merged = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i+=1

        else:
            merged.append(right[j])
            j+=1

    while i < len(left):
        merged.append(left[i])
        i+=1

    while j < len(right):
        merged.append(right[j])
        j+=1

    return merged




def mergeSort(arr):
    if (len(arr)) <=1:
        return arr

    mid = len(arr)//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)



arr = [3,4,1,32,452,900,0,34,52]
print(mergeSort(arr))