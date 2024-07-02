def BubbleSort(ls):
    for i in range(len(ls)):
        for j in range(0, len(ls) - i - 1):
            if ls[j] > ls[j + 1]:
                tmp = ls[j]
                ls[j] = ls[j + 1]
                ls[j + 1] = tmp

ls = [4, -5, 10, 7, -9]
BubbleSort(ls)
print(ls)