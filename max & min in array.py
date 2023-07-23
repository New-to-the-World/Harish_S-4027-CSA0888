def find_sum_and_difference(arr):
    max_num = max(arr)
    min_num = min(arr)
    sum_nums = max_num + min_num
    diff_nums = max_num - min_num
    return sum_nums, diff_nums

arr = [4, 7, 1, 9, 6]
sum_nums, diff_nums = find_sum_and_difference(arr)
print("Maximum number in array:", max(arr))
print("Minimum number in array:", min(arr))
print("Sum of maximum and minimum numbers in array:", sum_nums)
print("Difference between maximum and minimum numbers in array:", diff_nums)
