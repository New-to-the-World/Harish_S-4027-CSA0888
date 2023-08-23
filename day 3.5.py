def min_jumps_to_end(nums):
    n = len(nums)
    jumps = [float('inf')] * n
    jumps[0] = 0    
    for i in range(1, n):
        for j in range(i):
            if j + nums[j] >= i:
                jumps[i] = min(jumps[i], jumps[j] + 1)   
    if jumps[n - 1] == float('inf'):
        return -1
    else:
        return jumps[n - 1]

nums = [int(x) for x in input("Enter the array of integers separated by spaces: ").split()]
result = min_jumps_to_end(nums)
print("Minimum number of jumps:", result)
