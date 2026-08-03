class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        # """
        # for i in range(len(nums)):
        #     for j in range(len(nums)-1):
        #         if nums[j]>nums[j+1]:
        #             nums[j],nums[j+1]= nums[j+1],nums[j]
        # return nums
        

        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:

            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


        