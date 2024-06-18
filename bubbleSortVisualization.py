import matplotlib.pyplot as plt
import matplotlib.animation as animation

def bubble_sort(arr):
    n = len(arr)
    # Generator to yield the array after each swap
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                yield arr

def update_fig(arr, rects):
    for rect, val in zip(rects, arr):
        rect.set_height(val)

def bubble_sort_visualize(arr):
    fig, ax = plt.subplots()
    ax.set_title("Bubble Sort Visualization")
    bar_rects = ax.bar(range(len(arr)), arr, align="edge")
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, int(1.1 * max(arr)))
    
    anim = animation.FuncAnimation(
        fig, 
        func=update_fig, 
        fargs=(bar_rects,), 
        frames=bubble_sort(arr), 
        interval=100,
        repeat=False
    )
    plt.show()

# Example usage for visualization:
data = [64, 34, 25, 12, 22, 11, 90]
bubble_sort_visualize(data)
