class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def first_occur(nums,target):
            low = 0
            high = len(nums)-1
            ans = -1
            while low <= high :
                mid = (low+high)//2
                if target == nums[mid]:
                    ans = mid
                    high = mid-1
                elif target<nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            return ans
        def last_occur(nums,target):
            low = 0
            high = len(nums)-1
            ans= -1

            while low <= high :
                mid = (low+high)//2
                if target == nums[mid]:
                    ans = mid
                    low = mid+1
                elif target>nums[mid]:
                    low = mid+1
                else:
                    high = mid-1
            return ans
        return [first_occur(nums,target),last_occur(nums,target)]
       