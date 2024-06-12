def selectionSort(arr):
    n = len(arr)

    for i in range(n):
        minindex = i
        for j in range(i+1, n):
            if(arr[j]< arr[minindex]):
                minindex = j

        arr[minindex], arr[i] = arr[i], arr[minindex]

    return arr

def main():
    arr = [30,20,45,23,12,1,90,23]
    print(selectionSort(arr))

if __name__ == "__main__":
    main()