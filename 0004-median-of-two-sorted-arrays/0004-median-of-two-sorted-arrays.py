class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n_nums = nums1
        for num in nums2:
            n_nums.append(num)
        n_nums.sort()
        if len(n_nums)%2 == 0:  # evens
            ans = (n_nums[len(n_nums)//2-1]+n_nums[len(n_nums)//2])/2
        else:                   # odds
            ans = (n_nums[len(n_nums)//2])
        return ans