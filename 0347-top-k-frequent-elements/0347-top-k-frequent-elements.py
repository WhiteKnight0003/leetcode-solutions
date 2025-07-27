class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for val in nums:
            if d.get(val) == None:
                d[val] =1
            else:
                d[val] +=1
        list_ = sorted(d.items(), key = lambda item : item[1], reverse= True)
        res = []
        for item in list_[:k]:
            res.append(item[0])
        return res

        