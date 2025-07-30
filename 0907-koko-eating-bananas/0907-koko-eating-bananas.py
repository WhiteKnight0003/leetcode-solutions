class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        import math

        l, r = 1, max(piles)

        while(l<=r):
            sum_ = 0
            mid = (l+r)//2
            for i in piles:
                sum_ +=  math.ceil(i*1.0/mid)
            
            if sum_ <= h:
                r = mid -1
            else:
                l = mid +1
        return l
