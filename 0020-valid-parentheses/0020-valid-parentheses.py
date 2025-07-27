class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack =[]
        pair = {'{':'}', '(':')', '[':']'}
        if(len(s)==1):
            return False
        for i in s:
            if i in pair.keys():
                stack.append(i)
            else:
                if not stack or pair[stack.pop()] != i:
                    return False
        return not stack


        