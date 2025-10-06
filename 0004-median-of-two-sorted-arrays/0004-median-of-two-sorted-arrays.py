class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        i,j=0,0  
        res = []
        while i<len(nums1) and j<len(nums2):
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
        while(i<len(nums1)):
            res.append(nums1[i])
            i+=1
        while(j<len(nums2)):
            res.append(nums2[j])
            j+=1
        
        mid = (len(nums1)+len(nums2))//2
        check = (len(nums1)+len(nums2))%2
        if check:
            return res[mid]
        else:
            return (res[mid -1]+ res[mid])/2