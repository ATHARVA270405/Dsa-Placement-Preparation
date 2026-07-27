class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minimum = prices[0]
        max_price = 0
        for i in prices:
            minimum = min(minimum,i)
            profit = i - minimum
            max_price = max(max_price,profit)
        
        return max_price
            

        

