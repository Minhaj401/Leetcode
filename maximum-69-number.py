class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        num=str(num)
        num=num.replace("6","9",1)
        return int(num)