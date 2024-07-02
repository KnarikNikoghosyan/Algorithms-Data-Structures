def InsertionSort(ls):
    if len(ls) <= 1:
        return

    for i in range(1, len(ls)):
        n = ls[i]
        j = i - 1
        while j >= 0 and n < ls[j]:
            ls[j + 1] = ls[j]
            j -= 1
        ls[j + 1] = n

ls = [20, 15, 45, 7, 9]
InsertionSort(ls)
print(ls)