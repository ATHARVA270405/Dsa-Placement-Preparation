class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        low = max(weights)
        high = sum(weights) 
        while low <= high:
            mid = (low+high)//2
            days_used = 1
            current_weight = 0
            for weight in weights:
                if current_weight + weight > mid:
                       days_used += 1
                       current_weight = weight
                else:
                       current_weight += weight
            if days_used <= days:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
       
             








        