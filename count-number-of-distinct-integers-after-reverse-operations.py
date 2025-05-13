class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rev=[]
        for i in nums:
            a=str(i)
            a=a[::-1]
            a=int(a)
            rev.append(a)
        return len(set(nums+rev))