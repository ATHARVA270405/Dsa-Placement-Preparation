class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lst = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in lst:
                return [lst[complement],i]
            else :
                lst[nums[i]] = i