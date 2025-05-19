class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=1
        sum=0
        for i in str(n):
            if a==1:
                sum+=int(i)
                a=0
            elif a==0:
                sum-=int(i)
                a=1
        return sum