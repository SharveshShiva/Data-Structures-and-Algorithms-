def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

    return array

array = [56,78,9,45,23,8]
print("Original array:", array)
sorted_array = selection_sort(array)
print("Sorted array:", sorted_array)
