class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        tmp = 0
        d = {}
        for i in range(len(s)):
            c = s[i]
            if c in d and d[c] >= tmp:
                tmp = d[c]+1
            d[c]=i
            res = max(res, i-tmp+1)
        return res
        