class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        try:
            return nums.index(target)
        except:
            for i in range(len(nums)):
                print(i)
                if nums[i] - target > 0:
                    return i
                else: 
                    print( "hello", len(nums))
                    return len(nums)
