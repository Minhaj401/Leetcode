class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pr=1
        for i in nums:
            pr*=i
        if pr<0:
            return -1
        elif pr>0 :
            return 1
        else :
            return 0
        