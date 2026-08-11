class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        low = 1 
        high = max(nums)
        ans=0
        
        while low <= high:
            mid = (low+high)//2
            result = 0 
            for item in nums:
                result += (item+mid-1)//mid
            if result <= threshold:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans

    




        
        