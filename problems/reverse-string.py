class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        a=len(s)
        d=[]
        for i in range(a-1, -1, -1):
            d.append(s[i])
        s[:]=d

