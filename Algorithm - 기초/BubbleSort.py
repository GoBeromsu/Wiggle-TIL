def bubbleSort(numbers):
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp
    return numbers


def bubbleSortGpt(numbers):
    n = len(numbers)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
        if not swapped:
            break
    return numbers


print(bubbleSortGpt([2, 1, 5, 3, 4]))
print(bubbleSort([2, 1, 5, 3, 4]))
