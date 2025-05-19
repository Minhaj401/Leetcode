class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list2=[]
        for i in nums:
            list2.append(i*i)
        list2.sort()
        return list2 