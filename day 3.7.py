def permuteUnique(nums):
    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return      
        seen = set()
        for i in range(start, len(nums)):
            if nums[i] in seen:
                continue
            seen.add(nums[i])
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]           
    result = []
    backtrack(0)
    return result

user_input = input("Enter a list of numbers separated by spaces: ")
nums = [int(x) for x in user_input.split()]
unique_permutations = permuteUnique(nums)
for permutation in unique_permutations:
    print(permutation)
