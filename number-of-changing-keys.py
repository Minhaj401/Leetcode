class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=len(s)
        count=0
        s=s.lower()
        for i in range (l-1):
            if s[i]!=s[i+1]:
                count+=1
        return count