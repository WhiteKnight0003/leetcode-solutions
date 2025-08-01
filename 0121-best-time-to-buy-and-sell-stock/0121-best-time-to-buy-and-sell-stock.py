class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_ = 1e9
        max_ = 0
        min_idx = 0
        for i in range(len(prices)):
            if prices[i] < min_ : 
                min_ = prices[i]
            elif prices[i] -min_ >max_:
                max_= prices[i] - min_

        return max_
        