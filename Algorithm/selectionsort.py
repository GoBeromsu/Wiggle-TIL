def selection_sort(n):
    length = len(n)
    for i in range(length - 1):
        min_index = i
        for j in range(i + 1, length):
            if n[j] < n[min_index]:
                min_index = j
        if min_index != i:
            n[i], n[min_index] = n[min_index], n[i]
    return n

print(selection_sort([1, 4, 2, 3, 5]))
