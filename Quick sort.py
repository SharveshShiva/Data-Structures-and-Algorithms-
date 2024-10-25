def quick_sort(a):
    if len(a) <= 1:
        return a

    pivot = a[-1]
    left = [x for x in a[:-1] if x <= pivot]
    right = [x for x in a[:-1] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


a = [56,78,9,45,23,8]
print("Original array:", a)
sorted_a = quick_sort(a)
print("Sorted array:", sorted_a)
