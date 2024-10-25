def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

    return a

a = [56,78,9,45,23,8]
print("Original array:", a)
sorted_a = insertion_sort(a)
print("Sorted array:", sorted_a)


