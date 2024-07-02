# Binary search

def binary_search(list, num, left, right):
    if right >= left:
        mid = right + left // 2

        if list[mid] == num:
            return mid
        elif list[mid] > num:
            return binary_search(list, num, left, mid -1)
        else:
            return binary_search(list, num, mid + 1, right)

list = [1, 2, 3, 4, 5, 6, 7]
num = 4
res = binary_search(list, num, 0, len(list) -1)
print(res)


# Largest element in array

def find_max(list2, length):
    if  length == 1:
        return list2[0]
    return max(list2[length -1], find_max(list2, length - 1))

list2 = [4, 6, 9, 7, 1]
length = len(list2)
print(find_max(list2, length))

# k-th smallest number in array

def find_kth_smallest(list3, k):
    middle = list3[len(list3) // 2]
    left_part = [i for i in list3 if i < middle]
    right_part = [i for i in list3 if i > middle]
    
    if k <= len(left_part):
        return find_kth_smallest(left_part, k)
    elif k > len(list3) - len(right_part):
        return find_kth_smallest(right_part, k - (len(list3) - len(right_part)))

    else:
        return middle

list3 = [9, 13, 5, 2, 74, 56]
k = 3
print(find_kth_smallest(list3, k))