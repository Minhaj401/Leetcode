class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        for i in nums:
            if i%2==0:
                l.append(0)
            else:
                l.append(1)
        
        l.sort()
        return l