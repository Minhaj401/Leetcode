class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        single_sum = 0
        double_sum = 0
        total_sum = 0
        
        i = 0
        while i < len(nums):
            total_sum += nums[i]
            if nums[i] < 10:
                single_sum += nums[i]
            else:
                double_sum += nums[i]
            i += 1

        if single_sum > total_sum - single_sum:
            return True
        if double_sum > total_sum - double_sum:
            return True
        
        return False