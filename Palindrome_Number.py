class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a=str(x)
        if a[::-1]==a:
            return True
        else:
            return False