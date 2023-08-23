def shuffle(l1, l2):
    result = []
    min_len = min(len(l1), len(l2))    
    for i in range(min_len):
        result.append(l1[i])
        result.append(l2[i])   
    result.extend(l1[min_len:])
    result.extend(l2[min_len:])
    return result

list1 = list(map(int, input("Enter the elements of the first list separated by spaces: ").split()))
list2 = list(map(int, input("Enter the elements of the second list separated by spaces: ").split()))
shuffled_list = shuffle(list1, list2)
print("Shuffled list:", shuffled_list)
