class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        for j in range(len(nums)):
            for i in range (j):
                if nums[i]==nums[j] and i<j:
                    count+=1
        return count