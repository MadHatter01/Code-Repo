def quickSort(arr):
    if len(arr)<=1:
        return arr
    left, middle, right = [],[],[]

    pivot = arr[len(arr) // 2 ]

    for num in arr:
        if num < pivot:
            left.append(num)
        elif num == pivot:
            middle.append(num)
        else:
            right.append(num)

    return quickSort(left)+ middle + quickSort(right)



if __name__ == "__main__":
    arr = [2,3,1,34,242,29,40]

    print(f"Original array :{arr}")
    print(f"Sorted array: {quickSort(arr)}")