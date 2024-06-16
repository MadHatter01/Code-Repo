def insertionSort(arr):
    n = len(arr)

    for i in range(1, n):
        temp = arr[i]
        space = i-1

        while (space >=0 and arr[space] > temp ):
            arr[space+1] = arr[space]
            space -=1

        arr[space+1] = temp
    return arr


def main():
    arr = [45,2,3,24,1,454,900]
    print(insertionSort(arr))

if __name__=="__main__":
    main()



