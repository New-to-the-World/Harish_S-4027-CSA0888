def num_identical_pairs(nums):
    count = 0
    num_count = {}   
    for num in nums:
        if num in num_count:
            count += num_count[num]
            num_count[num] += 1
        else:
            num_count[num] = 1
    return count

nums = [int(x) for x in input("Enter the array of integers separated by spaces: ").split()]
result = num_identical_pairs(nums)
print("Number of good pairs:", result)
