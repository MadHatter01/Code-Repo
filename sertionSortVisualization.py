import matplotlib.pyplot as plt
import matplotlib.animation as animation

def insertionSort(arr):
    n = len(arr)

    for i in range(1, n):
        val = arr[i]
        space = i - 1

        while space >=0 and arr[space] > val:
            arr[space+1] = arr[space]
            space -=1
            yield arr
        
        arr[space + 1] = val
        yield arr
    yield arr



def update_fig(arr, rects):
    for rect, val in zip(rects, arr):
        rect.set_height(val)


def visualize(arr):
    fig, ax = plt.subplots();
    ax.set_title("Insertion sort visualization")

    bar_rects = ax.bar(range(len(arr)), arr, align = "edge") 

    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, int(1.1*max(arr)))

    anim = animation.FuncAnimation(
        fig,
        func = update_fig,
        fargs=(bar_rects,), 
        frames=insertionSort(arr), 
        interval=1000,
        repeat=False
    )

    plt.show()



def main():
    arr = [45, 2, 3, 24, 1, 454, 900]
    visualize(arr)

if __name__ == "__main__":
    main()