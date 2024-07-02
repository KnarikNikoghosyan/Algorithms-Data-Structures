def SelectionSort(ls):
    for i in range(0,len(ls) - 1):
        min_index = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[min_index]:
                min_index = j
        ls[min_index],ls[i] = ls[i], ls[min_index]
    print(ls)

ls = [ 5, 45, -545, 7, 59, -7, 12]
SelectionSort(ls)