class Solution(object):
    def returnToBoundaryCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        move=0
        for i in nums:
            move+=i
            if move ==0:
                count+=1
        return count
        