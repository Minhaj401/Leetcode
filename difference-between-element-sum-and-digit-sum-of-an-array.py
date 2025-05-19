class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ts=0
        s=0
        for i in nums:
            s+=i
        for i in nums:
            for j in str(i):
                ts+=int(j)
        return s-ts        