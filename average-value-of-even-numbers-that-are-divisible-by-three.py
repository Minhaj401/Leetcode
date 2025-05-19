class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        count=0
        for i in nums:
            if i%2==0 and i%3==0 :
                c+=i
                count+=1
        if count==0:
            return 0
        return c/count