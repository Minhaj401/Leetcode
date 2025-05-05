class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=[]
        for i in nums:
            if nums.count(i)==1:
                a.append(i)
       
        return sum(a)