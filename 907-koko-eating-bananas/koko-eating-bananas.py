class Solution(object):
    def minEatingSpeed(self, piles, h):
        def isPossible(speed):
            totalHours = 0

            for pile in piles:
                totalHours += (pile + speed - 1) // speed

            return totalHours <= h

        low = 1
        high = max(piles)
        ans = high

        while low <= high:
            mid = (low + high) // 2

            if isPossible(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans