class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        newNums = []
        for i in range(len(nums)-1):
            k = (nums[i] + nums[i+1]) % 10
            newNums.append(k)
            
        return self.triangularSum(newNums)