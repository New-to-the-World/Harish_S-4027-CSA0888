def merge_sorted_lists(list1, list2):
    merged = []
    i = j = 0   
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    merged.extend(list1[i:])
    merged.extend(list2[j:])    
    return merged

list1 = [int(x) for x in input("Enter the elements of the first sorted list separated by spaces: ").split()]
list2 = [int(x) for x in input("Enter the elements of the second sorted list separated by spaces: ").split()]
merged_list = merge_sorted_lists(list1, list2)
print("Merged and sorted list:", merged_list)
