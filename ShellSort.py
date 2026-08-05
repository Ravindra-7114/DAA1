def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
def print_array(arr):
    print(*arr)
n = int(input("Enter the size of the array: "))
arr = list(map(int, input(f"Enter {n} elements: ").split()))
print("Original Array:", end=" ")
print_array(arr)
shell_sort(arr)
print("Sorted Array:", end=" ")
print_array(arr)