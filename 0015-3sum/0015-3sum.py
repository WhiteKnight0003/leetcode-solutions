class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            if(nums[i]>0):
                break
            
            l, r = i+1, len(nums)-1
            while l <r:
                sum3= nums[l] + nums[r] + nums[i]
                if (sum3 ==0):
                    res.append([nums[i] , nums[l] , nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l+=1
                    while l<r and nums[r] == nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
                elif (sum3<0):
                    l+=1
                else:
                    r-=1
        return res
        