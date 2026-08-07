class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low= 0
        high = len(nums)-1
        idx = 0
        while low <= high :
            mid = (low+high)//2
            if nums[mid]==target:
                return mid
            elif target < nums[mid]:
                high = mid-1
                idx = mid
            else:
                low = mid+1
                idx = mid+1
        return idx
        