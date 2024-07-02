def CountingSort(ls):
    max_element = max(ls)
    count = [0] * (max_element + 1)
    length = max_element + 1

    for i in ls:
        count[i] += 1
    for j in range(1, length):
        count[j] += count[j - 1]

    output = [0] * len(ls)

    for j in range(len(ls) - 1, -1, -1):
        current_element = ls[j]
        count[current_element] -= 1
        new_position = count[current_element]
        output[new_position] = current_element
        i -= 1

    return output


ls = [3, 3, 8, 7, 0, 6, 6, 9]
print(CountingSort(ls))

