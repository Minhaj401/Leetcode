class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        a=0
        for i in str(x):
            a+=int(i)
        if x%a==0:
            return a
        else :
            return -1