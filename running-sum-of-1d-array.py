class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output=[]
        sum=0
        for i in nums:
            sum+=i
            output.append(sum)
        return output