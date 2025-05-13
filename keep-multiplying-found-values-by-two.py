class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        def find(nums,original):
            if original not in nums:
                return original
            return find(nums,original*2)
        return find(nums,original)