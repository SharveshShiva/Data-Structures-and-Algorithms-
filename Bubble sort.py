def bubble_sort(a):
    n = len(a)
    for i in range(n):
        swapped_element = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped_element = True
        if not swapped_element:
            break
    return a

a = [56,78,9,45,23,8]
print("Original array:", a)
sorted_a = bubble_sort(a)
print("Sorted array:", sorted_a)
