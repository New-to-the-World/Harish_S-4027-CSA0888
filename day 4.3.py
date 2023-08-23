def smallerNumbersThanCurrent(nums):
    count = [0] * 101 
    for num in nums:
        count[num] += 1    
    smaller_count = [0] * len(nums)
    for i in range(1, len(count)):
        count[i] += count[i - 1]   
    for i in range(len(nums)):
        if nums[i] > 0:
            smaller_count[i] = count[nums[i] - 1]  
    return smaller_count

nums = list(map(int, input("Enter the array of numbers separated by spaces: ").split()))
result = smallerNumbersThanCurrent(nums)
print(result)
