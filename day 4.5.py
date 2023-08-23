def minJumpsToEnd(nums):
    n = len(nums)
    if n <= 1:
        return 0
    jumps = [float('inf')] * n
    jumps[0] = 0
    for i in range(n):
        for j in range(i + 1, min(i + 1 + nums[i], n)):
            jumps[j] = min(jumps[j], jumps[i] + 1)
    return jumps[-1] if jumps[-1] != float('inf') else -1

nums = list(map(int, input("Enter the array of integers separated by spaces: ").split()))
result = minJumpsToEnd(nums)
print("Minimum number of jumps:", result)
