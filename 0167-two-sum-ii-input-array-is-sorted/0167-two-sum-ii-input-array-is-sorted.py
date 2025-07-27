class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r =0, len(numbers)-1
        while(l<r):
            res = numbers[l]+numbers[r] - target
            if(res==0):
                return [l+1,r+1]
            elif res>0:
                r-=1
            elif res <0:
                l+=1
        return []

        