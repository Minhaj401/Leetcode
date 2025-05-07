class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        a=[i for i in s.split()]
        b=len(a)-k
        for i in range(b):
            a.pop()
        s=" ".join(a)
        return s