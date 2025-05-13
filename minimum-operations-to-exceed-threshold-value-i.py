class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        while nums and min(nums) < k:
            nums.pop(nums.index(min(nums)))
            count += 1
        return count